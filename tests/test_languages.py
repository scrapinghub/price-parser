from decimal import Decimal

from pytest import mark

from price_parser import parse_price

@mark.parametrize(
    'locale,input_text,amount_text,amount',
    [
        # es
        ('es', '$ 4 millones', '4 millones', 4000000),
    ],
)
def test_localized_price_parsing(locale, input_text, amount_text, amount):
    price = parse_price(input_text, locale=locale)
    assert price.amount == Decimal(str(amount))
    assert price.amount_text == amount_text
