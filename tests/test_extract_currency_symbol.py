"""Unit tests for price_parser.parser.extract_currency_symbol.

Priority order (as implemented): dollar-codes (NZD, SGD, ...) when a "$" is
present, then "safe" symbols in the price, then safe symbols in the hint,
then other symbols in the price, then other symbols in the hint.
"""

import pytest

from price_parser.parser import extract_currency_symbol


@pytest.mark.parametrize(
    ("price", "hint", "expected"),
    [
        ("$12.99", None, "$"),
        ("12.99 €", None, "€"),
        ("£10", None, "£"),
        ("¥100", None, "¥"),
        ("₽100", None, "₽"),
        ("Kč 50", None, "Kč"),
        ("12.99 zł", None, "zł"),
        ("100 руб", None, "руб"),
        ("US$:12.99", None, "US$"),
        ("CA$10", None, "CA$"),
        ("HK$10", None, "HK$"),
        ("10 GBP", None, "GBP"),
        ("CHF 10", None, "CHF"),
        ("100円", None, "円"),
    ],
)
def test_currency_from_price_text(price, hint, expected):
    assert extract_currency_symbol(price, hint) == expected


@pytest.mark.parametrize(
    ("price", "hint", "expected"),
    [
        ("12.99", "$", "$"),
        ("12.99", "USD", "USD"),
        ("10", "GBP", "GBP"),
        ("50", "Kč", "Kč"),
        (None, "€", "€"),
    ],
)
def test_currency_from_hint(price, hint, expected):
    assert extract_currency_symbol(price, hint) == expected


@pytest.mark.parametrize(
    ("price", "hint", "expected"),
    [
        # Currency code attached to a dollar sign wins over the bare "$"
        ("NZD $123", None, "NZD"),
        ("SGD$5", None, "SGD"),
        ("123", "NZD $", "NZD"),
        ("5", "SGD$", "SGD"),
    ],
)
def test_dollar_codes_take_priority(price, hint, expected):
    assert extract_currency_symbol(price, hint) == expected


def test_safe_symbol_in_price_beats_hint():
    assert extract_currency_symbol("€12.99", "USD") == "€"
    assert extract_currency_symbol("$10", "EUR") == "$"


def test_safe_symbol_in_hint_beats_code_in_price():
    # Quirk: a "safe" symbol found in the hint (€) is preferred over a
    # 3-letter code found in the price text itself (USD), because safe
    # symbols are searched in both strings before unsafe ones.
    assert extract_currency_symbol("12.99 USD", "€") == "€"


@pytest.mark.parametrize(
    ("price", "hint"),
    [("12.99", None), ("hello", None), ("10 dollars", None), ("", ""), (None, None)],
)
def test_no_currency_found(price, hint):
    assert extract_currency_symbol(price, hint) is None
