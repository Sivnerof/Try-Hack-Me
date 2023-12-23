base_price = float(input("Enter cart total: "))

# Available coupon codes include 15% off and $12 off.
percent_discount = base_price - base_price * .15
fixed_discount = base_price - 12

# Pick the coupon that offers the best discount.
shipping_cost = float(input("Enter shipping cost: "))
final_price = round((min(fixed_discount, percent_discount) + shipping_cost),2)
print("Your best price is $" + str(final_price))

