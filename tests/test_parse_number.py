"""Unit tests for price_parser.parser.parse_number and get_decimal_separator.

The existing suite exercises these only indirectly through Price.fromstring
examples and the module doctests; here the number-format guessing rules are
pinned down directly.
"""

from decimal import Decimal

import pytest

from price_parser.parser import get_decimal_separator, parse_number


@pytest.mark.parametrize(
    ("num", "expected"),
    [
        ("0", Decimal("0")),
        ("999", Decimal("999")),
        ("0.00", Decimal("0.00")),
        ("-12.50", Decimal("-12.50")),
        ("3.14159", Decimal("3.14159")),
        ("1.2345", Decimal("1.2345")),
        (".5", Decimal("0.5")),
        ("5.", Decimal("5")),
        (" 42 ", Decimal("42")),
    ],
)
def test_parse_number_plain(num, expected):
    assert parse_number(num) == expected


@pytest.mark.parametrize(
    ("num", "expected"),
    [
        # A separator followed by exactly 3 digits is a group separator
        ("1,234", Decimal("1234")),
        ("12,345", Decimal("12345")),
        ("1.000.000", Decimal("1000000")),
        ("7,000,000", Decimal("7000000")),
        # ...followed by 1, 2 or 4+ digits it is a decimal separator
        ("12,5", Decimal("12.5")),
        ("12,34", Decimal("12.34")),
        # Both separators: the rightmost one is decimal
        ("1,234,567.89", Decimal("1234567.89")),
        ("1.234.567,89", Decimal("1234567.89")),
        ("1,234.5", Decimal("1234.5")),
        # Spaces are group separators and are simply removed
        ("1 234 567", Decimal("1234567")),
        ("1 234,99", Decimal("1234.99")),
        ("1 0", Decimal("10")),
    ],
)
def test_parse_number_grouped(num, expected):
    assert parse_number(num) == expected


@pytest.mark.parametrize(
    ("num", "expected"),
    [
        ("12€34", Decimal("12.34")),
        ("12 € 34", Decimal("12.34")),
        ("1,235€99", Decimal("1235.99")),
        ("1.235€99", Decimal("1235.99")),
    ],
)
def test_parse_number_euro_as_decimal_separator(num, expected):
    assert parse_number(num) == expected


def test_parse_number_leading_euro_sign_quirk():
    # A leading euro sign is also treated as the decimal separator,
    # so "€12" parses as 0.12 rather than 12.
    assert parse_number("€12") == Decimal("0.12")


@pytest.mark.parametrize(
    ("num", "decimal_separator", "expected"),
    [
        ("1,234", ".", Decimal("1234")),
        ("1,234", ",", Decimal("1.234")),
        ("1.234", ",", Decimal("1234")),
        ("1.234", ".", Decimal("1.234")),
        ("100", ",", Decimal("100")),
        ("140.000", ",", Decimal("140000")),
        ("140.000", ".", Decimal("140.000")),
    ],
)
def test_parse_number_explicit_decimal_separator(num, decimal_separator, expected):
    assert parse_number(num, decimal_separator=decimal_separator) == expected


@pytest.mark.parametrize("num", ["", " ", "abc", "12.34.56", "1,2,3", "1'234.50"])
def test_parse_number_unparseable_returns_none(num):
    # Note: the apostrophe group separator ("1'234.50") is only stripped by
    # extract_price_text, not by parse_number itself.
    assert parse_number(num) is None


@pytest.mark.parametrize(
    ("price", "expected"),
    [
        ("1000", None),
        ("12.99", "."),
        ("12,99", ","),
        ("12.999", None),  # 3 digits after the separator: group separator
        ("12,3456", ","),
        ("12.3456", "."),
        ("1.500,25", ","),
        ("1,500.25", "."),
        ("1,235€99", "€"),
        (".75", "."),
        ("5.", None),
        ("abc", None),
        ("", None),
        ("1.234.567", None),
    ],
)
def test_get_decimal_separator(price, expected):
    assert get_decimal_separator(price) == expected
