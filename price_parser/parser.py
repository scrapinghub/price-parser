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
                   currency_hint: Optional[str] = None,
                   decimal_separator: Optional[str] = None) -> 'Price':
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
        amount_num = (
            parse_number(amount_text, decimal_separator)
            if amount_text is not None else None
        )
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
    '$U', 'C$', 'J$', 'N$', 'R$', 'S$', 'T$', 'Z$', 'A$',
    'SY£', 'LB£', 'CN¥', 'GH₵',

    # unique currency symbols
    '$', '€', '£', 'zł', 'Zł', 'Kč', '₽', '¥', '￥',
    '฿', 'դր.', 'դր', '₦', '₴', '₱', '৳', '₭', '₪',  '﷼', '៛', '₩', '₫', '₡',
    'টকা', 'ƒ', '₲', '؋', '₮', 'नेरू', '₨',
    '₶', '₾', '֏', 'ރ', '৲', '૱', '௹', '₠', '₢', '₣', '₤', '₧', '₯',
    '₰', '₳', '₷', '₸', '₹', '₺', '₼', '₾', '₿', 'ℳ',
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
_DOLLAR_REGEX = re.compile(
    r'''
        \b
        (?:{})  # currency code like NZD
        (?=
            \$?  # dollar sign to ignore if attached to the currency code
            (?:[\W\d]|$)  # not a letter
        )
    '''.format('|'.join(re.escape(k) for k in DOLLAR_CODES)),
    re.VERBOSE,
)


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

_search_dollar_code = _DOLLAR_REGEX.search
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


# word: (scale, increment)
_NUMBER_WORDS = {
    word: (Decimal(scale), Decimal(increment)) for word, scale, increment in
    (
        ('zero', 1, 0),
        ('one', 1, 1),
        ('two', 1, 2),
        ('three', 1, 3),
        ('four', 1, 4),
        ('five', 1, 5),
        ('six', 1, 6),
        ('seven', 1, 7),
        ('eight', 1, 8),
        ('nine', 1, 9),
        ('ten', 1, 10),
        ('eleven', 1, 11),
        ('twelve', 1, 12),
        ('thirteen', 1, 13),
        ('fourteen', 1, 14),
        ('fifteen', 1, 15),
        ('sixteen', 1, 16),
        ('seventeen', 1, 17),
        ('eighteen', 1, 18),
        ('nineteen', 1, 19),
        ('twenty', 1, 20),

        ('thirty', 1, 30),
        ('forty', 1, 40),
        ('fifty', 1, 50),
        ('sixty', 1, 60),
        ('seventy', 1, 70),
        ('eighty', 1, 80),
        ('ninety', 1, 90),

        ('hundred', 100, 0),
        ('thousand', 10 ** 3, 0),
        ('million', 10 ** 6, 0),
        ('billion', 10 ** 9, 0),
        ('trillion', 10 ** 12, 0),

        ('and', 1, 0),
    )
}
_NUMBER_WORDS_PATTERN = r'(?:{})'.format('|'.join(_NUMBER_WORDS))


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
    '35€ 99'
    >>> extract_price_text("35€ 999")
    '35'
    >>> extract_price_text("1,235€ 99")
    '1,235€ 99'
    >>> extract_price_text("50% OFF")
    >>> extract_price_text("50%")
    >>> extract_price_text("50")
    '50'
    >>> extract_price_text("$1\xa0298,00")
    '1 298,00'
    >>> extract_price_text("$.75")
    '.75'
    >>> extract_price_text("$ 4 million")
    '4 million'
    >>> extract_price_text("four million")
    'four million'
    >>> extract_price_text("1 thousand 35€ 99")
    '1 thousand 35€ 99'
    """
    price = re.sub(r'\s+', ' ', price)  # clean initial text from non-breaking and extra spaces

    m = None
    if price.count('€') == 1:
        m = re.search(r"""
        (
            (?:
                [\d\s.,]|   # number, probably with thousand separators
                {}          # numeric English words
            )*?
            \d              # there must be a a digit before €
            \s*?€(\s*?)?    # euro, probably separated by whitespace
            \d(?(2)\d|\d*?) # if separated by whitespace - search one digit, multiple digits otherwise
        )
        (?:$|[^\d])    # something which is not a digit
        """.format(_NUMBER_WORDS_PATTERN), price, re.VERBOSE)

    if not m:
        m = re.search(r"""
            (
                (?:
                    \d|        # number, as a digit
                    {0}        # numeric English words
                )
                (?:
                    [\d\s.,]|  # number, probably with thousand separators
                    {0}        # numeric English words
                )*
            )
            \s*?               # skip whitespace
            (?:[^%\d]|$)       # capture next symbol - it shouldn't be %
            """.format(_NUMBER_WORDS_PATTERN), price, re.VERBOSE)

    if m:
        price_text = m.group(1).rstrip(',.')
        return (
            price_text.strip()
            if price_text.count('.') == 1
            else price_text.lstrip(',.').strip()
        )

    if 'free' in price.lower():
        return '0'

    return None


# NOTE: Keep supported separators in sync with parse_number()
_search_decimal_sep = re.compile(r"""
\d*          # null or more digits (there can be more before it)
([.,€])      # decimal separator
(?:          # 1,2 or 4+ digits. 3 digits is likely to be a thousand separator.
   \d{1,2}?|
   \d{4}\d*?
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
    >>> get_decimal_separator(".75")
    '.'
    """
    m = _search_decimal_sep(price)
    if m:
        return m.group(1)


# Based on https://stackoverflow.com/a/493788/939364
def _words_to_digits(words):
    """Given a string containing a number in English, or a combination of
    English and digits (e.g. ‘3 million’), return the corresponding number as a
    ``Decimal``.

    In the input string, thousand separators must not exist, and if there are
    decimals, a dot (.) must be used as decimal separator, and there must be
    digits at either side of the decimal separator.

    ``None`` is return on invalid input.

    >>> parse_number("1234")
    Decimal('1234')
    >>> parse_number("12.34")
    Decimal('12.34')
    >>> parse_number("4 million")
    Decimal('4000000')
    >>> parse_number("four million")
    Decimal('4000000')
    >>> parse_number("")
    >>> parse_number(" ")
    >>> parse_number("foo")
    """
    if not words.strip():
        return None

    current = result = Decimal(0)
    for word in words.split():
        try:
            scale, increment = _NUMBER_WORDS[word]
            is_word = True
        except KeyError:
            try:
                increment = Decimal(word)
            except InvalidOperation:
                return None
            match = re.match(r'\d+', word)
            assert match is not None
            scale = Decimal(10) ** len(match[0])
            is_word = False

        current = current * scale + increment
        if scale > Decimal(100) and is_word:
            result += current
            current = Decimal(0)

    return result + current


def parse_number(num: str,
                 decimal_separator: Optional[str] = None) -> Optional[Decimal]:
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
    >>> parse_number("140.000", decimal_separator=",")
    Decimal('140000')
    >>> parse_number("140.000", decimal_separator=".")
    Decimal('140.000')
    >>> parse_number("4 million")
    Decimal('4000000')
    >>> parse_number("four million")
    Decimal('4000000')
    >>> parse_number("")
    >>> parse_number("foo")
    """
    if not num:
        return None

    num = num.strip()
    num = re.sub(r'\s+(?=\W)|(?<=\W)\s+', '', num)
    decimal_separator = decimal_separator or get_decimal_separator(num)
    # NOTE: Keep supported separators in sync with _search_decimal_sep
    if decimal_separator is None:
        num = num.replace('.', '').replace(',', '')
    elif decimal_separator == '.':
        num = num.replace(',', '')
    elif decimal_separator == ',':
        num = num.replace('.', '').replace(',', '.')
    else:
        assert decimal_separator == '€'
        num = num.replace('.', '').replace(',', '').replace('€', '.')

    return _words_to_digits(num)
