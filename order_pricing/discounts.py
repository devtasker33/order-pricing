"""Discount codes applied to the order subtotal."""
from order_pricing.config import DISCOUNT_CODES, MAX_DISCOUNT_PCT


def discount_amount(subtotal, code):
    """Amount taken off the subtotal for a discount code, capped at MAX_DISCOUNT_PCT."""
    if not code:
        return 0
    pct = min(DISCOUNT_CODES.get(code, 0), MAX_DISCOUNT_PCT)
    return round(subtotal * pct / 100, 2)


def cart_price_with_code(subtotal, code):
    """Price shown on the cart page once a code is typed in (VAT included)."""
    from order_pricing.pricing import apply_tax
    return apply_tax(subtotal - discount_amount(subtotal, code))
