"""Business settings for order pricing."""

TAX_RATE = 0.20
SHIPPING_FEE = 4.90
FREE_SHIPPING_THRESHOLD = 35

# Discount codes: code -> percent off the subtotal
DISCOUNT_CODES = {"WELCOME10": 10, "SPRING15": 15, "STAFF50": 50}
MAX_DISCOUNT_PCT = 30
