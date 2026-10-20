"""Order pricing: subtotal, VAT, shipping and total."""
from order_pricing.config import TAX_RATE, SHIPPING_FEE, FREE_SHIPPING_THRESHOLD


def subtotal(items):
    """Sum of price x quantity for every line of the order."""
    return sum(item["price"] * item["qty"] for item in items)


def apply_tax(amount, rate=TAX_RATE):
    """Add VAT to an amount."""
    return amount * (1 + rate)


def shipping(amount):
    """Shipping fee, free above the threshold."""
    return 0 if amount >= FREE_SHIPPING_THRESHOLD else SHIPPING_FEE


def compute_total(order):
    """Total the customer pays: subtotal + VAT + shipping."""
    sub = subtotal(order["items"])
    total = apply_tax(sub) + shipping(sub)
    return total
