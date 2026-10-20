from order_pricing import pricing


def test_subtotal():
    items = [{"price": 10.0, "qty": 2}, {"price": 5.0, "qty": 1}]
    assert pricing.subtotal(items) == 25.0


def test_total_with_shipping():
    order = {"items": [{"price": 10.0, "qty": 1}]}
    assert pricing.compute_total(order) == 16.9
