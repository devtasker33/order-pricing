from order_pricing import discounts, pricing


def test_discount_amount():
    assert discounts.discount_amount(50.0, "WELCOME10") == 5.0


def test_discount_is_capped():
    assert discounts.discount_amount(100.0, "STAFF50") == 30.0


def test_unknown_code_gives_no_discount():
    assert discounts.discount_amount(100.0, "NOPE") == 0


def test_cart_price_with_code():
    assert discounts.cart_price_with_code(50.0, "WELCOME10") == 54.0


def test_total_with_code():
    order = {"items": [{"price": 50.0, "qty": 1}], "discount_code": "WELCOME10"}
    assert pricing.compute_total(order) == 54.0
