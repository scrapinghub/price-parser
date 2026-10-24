"""Sanity tests for the price_parser._currencies data tables.

These guard the data the parser's regexes are built from: ISO codes are
unique 3-letter uppercase strings, and the symbol tables are populated.
"""

from price_parser._currencies import (
    CURRENCIES,
    CURRENCY_CODES,
    CURRENCY_NATIONAL_SYMBOLS,
    CURRENCY_SYMBOLS,
)


def test_currency_codes_are_unique_three_letter_uppercase():
    assert len(CURRENCY_CODES) == len(set(CURRENCY_CODES))
    assert all(len(code) == 3 and code.isalpha() and code.isupper() for code in CURRENCY_CODES)


def test_well_known_codes_present():
    for code in ["USD", "EUR", "GBP", "JPY", "CHF", "PLN", "CZK", "RUB", "CNY"]:
        assert code in CURRENCY_CODES


def test_codes_match_currencies_table():
    assert set(CURRENCY_CODES) == set(CURRENCIES.keys())
    assert len(CURRENCY_CODES) > 150


def test_symbol_tables_populated():
    assert "€" in CURRENCY_SYMBOLS
    assert "$" in CURRENCY_SYMBOLS
    assert "£" in CURRENCY_SYMBOLS
    assert len(CURRENCY_SYMBOLS) > 50
    assert len(CURRENCY_NATIONAL_SYMBOLS) > 50


def test_every_currency_entry_has_a_symbol():
    assert all(info["s"] for info in CURRENCIES.values())
