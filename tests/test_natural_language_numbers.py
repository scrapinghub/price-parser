from decimal import Decimal

import pytest

from price_parser import parse_price


@pytest.mark.parametrize(
    ("input_text", "amount_text", "amount"),
    [
        ("$ 4 million", "4 million", 4000000),
        ("$ four million", "four million", 4000000),
        ("$ four million dollars", "four million", 4000000),
        ("$ 400 thousand", "400 thousand", 400000),
        ("$ 1 thousand 999 € 99", "1 thousand 999 € 99", "1999.99"),
    ],
)
def test_price_parsing(input_text: str, amount_text: str, amount: "int | str") -> None:
    price = parse_price(input_text)
    assert (price.amount_text, price.amount) == (amount_text, Decimal(amount))
