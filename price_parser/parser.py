# -*- coding: utf-8 -*-
import re
import string
from typing import Callable, Optional, Pattern, List, Tuple
from decimal import Decimal, InvalidOperation

import attr
from ._currencies import (CURRENCY_CODES, CURRENCY_NATIONAL_SYMBOLS,
                          CURRENCY_SYMBOLS)


@attr.s(auto_attribs=True)
class Price:
    amount: Optional[Decimal]   # price numeric value, as Decimal
    currency: Optional[str]     # currency symbol (as appeared in text)

    # price value, as a raw string
    amount_text: Optional[str] = attr.ib(repr=False)

    @property
    def amount_float(self) -> Optional[float]:
        """ price numeric value, as float """
        if self.amount is not None:
            return float(self.amount)

    @classmethod
    def fromstring(cls, price: Optional[str],
                   currency_hint: Optional[str] = None) -> 'Price':
        """
        Given price and currency text extracted from HTML elements, return
        ``Price`` instance, which provides a clean currency symbol and
        price amount as a Decimal number.

        ``currency_hint`` is optional; you can pass value of some element
        which may contain currency, as a hint. If currency is present in
        ``price`` string, it could be **preferred** over a value extracted
        from ``currency_hint`` string.
        """
        amount_text = extract_price_text(price) if price is not None else None
        amount_num = parse_number(amount_text) if amount_text is not None else None
        currency = extract_currency_symbol(price, currency_hint)
        if currency is not None:
            currency = currency.strip()
        return Price(
            amount=amount_num,
            currency=currency,
            amount_text=amount_text,
        )


parse_price = Price.fromstring


def or_regex(symbols: List[str]) -> Pattern:
    """ Return a regex which matches any of ``symbols`` """
    return re.compile('|'.join(re.escape(s) for s in symbols))


# If one of these symbols is found either in price or in currency,
# it is considered currency symbol, and returned as a currency, regardless
# of its position in text.
SAFE_CURRENCY_SYMBOLS = [
    # Variants of $, etc. They need to be before $.
    'Bds$', 'CUC$', 'MOP$',
    'AR$', 'AU$', 'BN$', 'BZ$', 'CA$', 'CL$', 'CO$', 'CV$', 'HK$', 'MX$',
    'NT$', 'NZ$', 'TT$', 'RD$', 'WS$', 'US$',
    '$U', 'C$', 'J$', 'N$', 'R$', 'S$', 'T$', 'Z$',
    'SY£', 'LB£', 'CN¥', 'GH₵',

    # unique currency symbols
    '$', '€', '£', 'zł', 'Zł', 'Kč', '₽', '¥', '￥',
    '฿', 'դր.', 'դր', '₦', '₴', '₱', '৳', '₭', '₪',  '﷼', '៛', '₩', '₫', '₡',
    'টকা', 'ƒ', '₲', '؋', '₮', 'नेरू', '₨',
    'ر.ق.\u200f', 'د.ك.\u200f', 'د.ع.\u200f', 'ر.ع.\u200f', 'ر.ي.\u200f',
    'ر.س.\u200f', 'د.ج.\u200f', 'د.م.\u200f', 'د.إ.\u200f', 'د.ت.\u200f',
    'د.ل.\u200f', 'ل.س.\u200f', 'د.ب.\u200f', 'د.أ.\u200f', 'ج.م.\u200f',
    'ل.ل.\u200f',

    ' تومان', 'تومان',

    # other common symbols, which we consider unambiguous
    'EUR', 'euro', 'eur', 'CHF', 'DKK', 'Rp', 'lei',
    'руб.', 'руб',  'грн.', 'грн', 'дин.', 'Dinara', 'динар', 'лв.', 'лв',
    'р.', 'тңг', 'тңг.', 'ман.',
]

# "D" in some abbreviations means "dollar", and so currency
# can be written as SGD$123 or NZD $123. Currency code should take priority
# over $ symbol in this case.
DOLLAR_CODES = [k for k in CURRENCY_CODES if k.endswith('D')]
DOLLAR_REGEXES = [
    r"""
    \b{}   # code like NZD
    (?:[^\w]|$)  # not a letter
    """.format(k) for k in DOLLAR_CODES
]


# Other common currency symbols: 3-letter codes, less safe abbreviations
OTHER_CURRENCY_SYMBOLS_SET = (
    set(
        CURRENCY_CODES +
        CURRENCY_SYMBOLS +
        CURRENCY_NATIONAL_SYMBOLS +

        # even if they appear in text, currency is likely to be rouble
        ['р', 'Р']
    )
    - set(SAFE_CURRENCY_SYMBOLS)   # already handled
    - {'-', 'XXX'}                 # placeholder values
    - set(string.ascii_uppercase)  # very unreliable on their own
)
OTHER_CURRENCY_SYMBOLS = sorted(OTHER_CURRENCY_SYMBOLS_SET,
                                key=len, reverse=True)

_search_dollar_code = re.compile("|".join(DOLLAR_REGEXES), re.VERBOSE).search
_search_safe_currency = or_regex(SAFE_CURRENCY_SYMBOLS).search
_search_unsafe_currency = or_regex(OTHER_CURRENCY_SYMBOLS).search


def extract_currency_symbol(price: Optional[str],
                            currency_hint: Optional[str]) -> Optional[str]:
    """
    Guess currency symbol from extracted price and currency strings.
    Return an empty string if symbol is not found.
    """
    methods: List[Tuple[Callable, Optional[str]]] = [
        (_search_safe_currency, price),
        (_search_safe_currency, currency_hint),
        (_search_unsafe_currency, price),
        (_search_unsafe_currency, currency_hint),
    ]

    if currency_hint and '$' in currency_hint:
        methods.insert(0, (_search_dollar_code, currency_hint))

    if price and '$' in price:
        methods.insert(0, (_search_dollar_code, price))

    for meth, attr in methods:
        m = meth(attr) if attr else None
        if m:
            return m.group(0)

    return None


def extract_price_text(price: str) -> Optional[str]:
    """
    Extract text of a price from a string which contains price and
    maybe some other text. If multiple price-looking substrings are present,
    the first is returned (FIXME: it is better to return a number
    which is near a currency symbol).

    >>> extract_price_text("price: $12.99")
    '12.99'
    >>> extract_price_text("Free")
    '0'
    >>> extract_price_text("Foo")
    >>> extract_price_text("1,235 USD")
    '1,235'

    In addition to numbers, it has a limited support for a case where
    currency symbol (currently only euro) is a decimal separator:

    >>> extract_price_text("99 €, 79 €")
    '99'
    >>> extract_price_text("99 € 79 €")
    '99'
    >>> extract_price_text("35€ 99")
    '35€99'
    >>> extract_price_text("35€ 999")
    '35'
    >>> extract_price_text("1,235€ 99")
    '1,235€99'
    >>> extract_price_text("50% OFF")
    >>> extract_price_text("50%")
    >>> extract_price_text("50")
    '50'
    """
    if price.count('€') == 1:
        m = re.search(r"""
        [\d\s.,]*\d    # number, probably with thousand separators
        \s*€\s*        # euro, probably separated by whitespace
        \d\d
        (?:$|[^\d])    # something which is not a digit
        """, price, re.VERBOSE)
        if m:
            return m.group(0).replace(' ', '')
    m = re.search(r"""
        (\d[\d\s.,]*)  # number, probably with thousand separators
        \s*            # skip whitespace
        (?:[^%\d]|$)   # capture next symbol - it shouldn't be %
        """, price, re.VERBOSE)

    if m:
        return m.group(1).strip(',.').strip()
    if 'free' in price.lower():
        return '0'
    return None


_search_decimal_sep = re.compile(r"""
\d           # at least one digit (there can be more before it)
([.,€])      # decimal separator
(?:          # 1,2 or 4 digits. 3 digits is likely to be a thousand separator.
   \d{1,2}|
   \d{4}
)
$
""", re.VERBOSE).search


def get_decimal_separator(price: str) -> Optional[str]:
    """ Return decimal separator symbol or None if there
    is no decimal separator.

    >>> get_decimal_separator("1000")
    >>> get_decimal_separator("12.99")
    '.'
    >>> get_decimal_separator("12,99")
    ','
    >>> get_decimal_separator("12.999")
    >>> get_decimal_separator("3,0000")
    ','
    >>> get_decimal_separator("1,235€99")
    '€'
    """
    m = _search_decimal_sep(price)
    if m:
        return m.group(1)


def parse_number(num: str) -> Optional[Decimal]:
    """ Parse a string with a number to a Decimal, guessing its format:
    decimal separator, thousand separator. Return None if parsing fails.

    >>> parse_number("1,234")
    Decimal('1234')
    >>> parse_number("12,34")
    Decimal('12.34')
    >>> parse_number("12,345")
    Decimal('12345')
    >>> parse_number("1,1")
    Decimal('1.1')
    >>> parse_number("1.1")
    Decimal('1.1')
    >>> parse_number("1234")
    Decimal('1234')
    >>> parse_number("12€34")
    Decimal('12.34')
    >>> parse_number("12€ 34")
    Decimal('12.34')
    >>> parse_number("1 234.99")
    Decimal('1234.99')
    >>> parse_number("1,235€99")
    Decimal('1235.99')
    >>> parse_number("1 235€99")
    Decimal('1235.99')
    >>> parse_number("1.235€99")
    Decimal('1235.99')
    >>> parse_number("")
    >>> parse_number("foo")
    """
    if not num:
        return None
    num = num.strip().replace(' ', '')
    decimal_separator = get_decimal_separator(num)
    if decimal_separator is None:
        num = num.replace('.', '').replace(',', '')
    elif decimal_separator == '.':
        num = num.replace(',', '')
    elif decimal_separator == ',':
        num = num.replace('.', '').replace(',', '.')
    elif decimal_separator == '€':
        num = num.replace('.', '').replace(',', '').replace('€', '.')
    try:
        return Decimal(num)
    except InvalidOperation:
        return None
