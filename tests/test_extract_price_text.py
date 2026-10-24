"""Unit tests for price_parser.parser.extract_price_text.

Covers the first-match rule, the percent exclusion, the "free" shortcut,
non-breaking-space normalisation and the euro-as-decimal-separator form.
"""

import pytest

from price_parser.parser import extract_price_text


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        ("$12.99", "12.99"),
        ("price: $12.99", "12.99"),
        ("price is 12.99 USD", "12.99"),
        ("1,235 USD", "1,235"),
        ("USD 1,299.95", "1,299.95"),
        ("12,99 €", "12,99"),
        ("1.299,00 €", "1.299,00"),
        ("€ 0,50", "0,50"),
        ("only 5", "5"),
        ("50", "50"),
        ("$.75", ".75"),
        # The first price-looking substring wins
        ("from $9.99 to $19.99", "9.99"),
        # Non-breaking spaces are normalised to regular spaces
        ("$1\xa0298,00", "1 298,00"),
        ("1 299,00 zł", "1 299,00"),
    ],
)
def test_extract_price_text_basic(text, expected):
    assert extract_price_text(text) == expected


@pytest.mark.parametrize(
    ("text", "expected"),
    [
        # Euro sign used as the decimal separator
        ("35€ 99", "35€99"),
        ("1,235€ 99", "1,235€99"),
        # With two euro prices the first amount is returned bare
        ("99 €, 79 €", "99"),
        ("99 € 79 €", "99"),
        ("35€ 999", "35"),
    ],
)
def test_extract_price_text_euro_separator(text, expected):
    assert extract_price_text(text) == expected


@pytest.mark.parametrize("text", ["50% OFF", "50%", "Foo", "no digits here", ""])
def test_extract_price_text_no_price(text):
    assert extract_price_text(text) is None


def test_extract_price_text_percent_number_is_skipped():
    # The "20%" is not a price, but the parser still finds the later amount
    assert extract_price_text("save 20% now 15.00") == "15.00"


@pytest.mark.parametrize("text", ["Free", "free shipping", "FREE!"])
def test_extract_price_text_free_means_zero(text):
    assert extract_price_text(text) == "0"
