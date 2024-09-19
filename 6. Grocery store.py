item_prices = [5.00, 12.50, 3.75, 7.00] 
quantities = [2, 1, 4, 3] 
discount_rate = 10 
tax_rate = 5 
subtotal = sum(price * qty for price, qty in zip(item_prices, quantities))
discount_amount = (discount_rate / 100) * subtotal
discounted_total = subtotal - discount_amount
tax_amount = (tax_rate / 100) * discounted_total
total_cost = discounted_total + tax_amount
print(f"Subtotal: ${subtotal:.2f}")
print(f"Discount: -${discount_amount:.2f}")
print(f"Tax: +${tax_amount:.2f}")
print(f"Total cost: ${total_cost:.2f}")
