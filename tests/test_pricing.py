from order_pricing import pricing


def test_subtotal():
    items = [{"price": 10.0, "qty": 2}, {"price": 5.0, "qty": 1}]
    assert pricing.subtotal(items) == 25.0


def test_total_with_shipping():
    order = {"items": [{"price": 10.0, "qty": 1}]}
    assert pricing.compute_total(order) == 16.9


def test_vat_is_rounded_to_the_cent():
    assert pricing.add_vat(10.01) == 12.01


def test_free_shipping_starts_at_40():
    assert pricing.shipping(39.99) == 4.90
    assert pricing.shipping(40.0) == 0


def test_empty_order_is_rejected():
    import pytest
    with pytest.raises(ValueError):
        pricing.compute_total({"items": []})
