"""Order pricing: subtotal, VAT, shipping and total."""
from order_pricing.config import TAX_RATE, SHIPPING_FEE, FREE_SHIPPING_THRESHOLD


def subtotal(items):
    """Sum of price x quantity for every line of the order."""
    return sum(item["price"] * item["qty"] for item in items)


def add_vat(amount, rate=TAX_RATE):
    """Add VAT to an amount, rounded to the cent."""
    return round(amount * (1 + rate), 2)


def shipping(amount):
    """Shipping fee, free above the threshold."""
    return 0 if amount >= FREE_SHIPPING_THRESHOLD else SHIPPING_FEE


def compute_total(order):
    """Total the customer pays: subtotal + VAT + shipping."""
    if not order["items"]:
        raise ValueError("order has no items")
    sub = subtotal(order["items"])
    total = add_vat(sub) + shipping(sub)
    return round(total, 2)
