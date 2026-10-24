"""Tests for the Price object itself: construction, equality, amount_float,
the parse_price alias and Price.fromstring parameter handling.

The big example tables in test_price_parsing.py cover end-to-end parsing;
these pin down object-level behaviour instead.
"""

from decimal import Decimal

import pytest

from price_parser import Price, parse_price


def test_parse_price_alias_matches_fromstring():
    assert parse_price("$12.99") == Price.fromstring("$12.99")
    assert parse_price("1,234.56 USD") == Price.fromstring("1,234.56 USD")


def test_public_api():
    import price_parser

    assert price_parser.__all__ == ["Price", "parse_price"]


@pytest.mark.parametrize("raw", [None, "", "   "])
def test_fromstring_no_price(raw):
    price = Price.fromstring(raw)
    assert price.amount is None
    assert price.currency is None
    assert price.amount_text is None
    assert price.amount_float is None


def test_fromstring_fields():
    price = Price.fromstring("$12.99")
    assert price.amount == Decimal("12.99")
    assert price.currency == "$"
    assert price.amount_text == "12.99"
    assert price.amount_float == 12.99


def test_amount_float_property():
    assert Price(Decimal("2.50"), None, "2.50").amount_float == 2.5
    assert Price(Decimal("0"), None, "0").amount_float == 0.0
    assert Price(None, None, None).amount_float is None


def test_equality_includes_amount_text():
    # Price is an attrs class: all three fields take part in equality,
    # including amount_text.
    assert Price(Decimal("1.00"), "$", "1.00") == Price(Decimal("1.00"), "$", "1.00")
    assert Price(Decimal("1.00"), "$", "1.00") != Price(Decimal("1.00"), "$", "1.0")
    assert Price(Decimal("1.00"), "$", "1.00") != Price(Decimal("2.00"), "$", "1.00")
    assert Price(Decimal("1.00"), "$", "1.00") != Price(Decimal("1.00"), "€", "1.00")


def test_repr_shows_amount_and_currency_only():
    # amount_text is excluded from the repr (repr=False)
    assert repr(Price.fromstring("$12.99")) == "Price(amount=Decimal('12.99'), currency='$')"


def test_currency_hint_used_when_price_has_no_currency():
    price = Price.fromstring("12.99", currency_hint="USD")
    assert price.currency == "USD"
    assert price.amount == Decimal("12.99")


def test_currency_in_price_beats_hint():
    assert Price.fromstring("€12.99", currency_hint="USD").currency == "€"


def test_currency_is_stripped():
    assert Price.fromstring("12.99", currency_hint=" $ ").currency == "$"


def test_free_price_is_zero():
    price = Price.fromstring("Free")
    assert price.amount == Decimal("0")
    assert price.amount_text == "0"
    assert price.currency is None


def test_percent_text_has_no_price():
    price = Price.fromstring("50% OFF")
    assert price.amount is None
    assert price.amount_text is None


def test_unparseable_amount_keeps_text_but_no_amount():
    price = Price.fromstring("12.99.99")
    assert price.amount is None
    assert price.amount_text == "12.99.99"


def test_digit_group_separator_parameter():
    assert Price.fromstring("1.234", digit_group_separator=".").amount == Decimal("1234")
    assert Price.fromstring("1,234", digit_group_separator=",").amount == Decimal("1234")


def test_decimal_separator_parameter():
    assert Price.fromstring("1.000", decimal_separator=",").amount == Decimal("1000")
    assert Price.fromstring("1.000", decimal_separator=".").amount == Decimal("1.000")


def test_swiss_apostrophe_group_separator_end_to_end():
    price = Price.fromstring("CHF 1'049,95")
    assert price.amount == Decimal("1049.95")
    assert price.amount_text == "1049,95"
    assert price.currency == "CHF"


def test_euro_cents_end_to_end():
    price = Price.fromstring("35€ 99")
    assert price.amount == Decimal("35.99")
    assert price.currency == "€"
