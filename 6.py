
item_prices = [2.5, 3.0, 1.75, 4.25]  
item_quantities = [3, 2, 4, 1]
discount_rate = 10
tax_rate = 8        

# Step 1: Calculate the subtotal
subtotal = sum(price * quantity for price, quantity in zip(item_prices, item_quantities))

# Step 2: Calculate the discount amount
discount_amount = (discount_rate / 100) * subtotal

# Step 3: Calculate the discounted subtotal
discounted_subtotal = subtotal - discount_amount

# Step 4: Calculate the tax amount
tax_amount = (tax_rate / 100) * discounted_subtotal

# Step 5: Calculate the total cost
total_cost = discounted_subtotal + tax_amount

# Print the total cost
print("Total cost", total_cost)
