import numpy as np
sales_data = np.array([[10, 20, 30],
                       [15, 25, 35],
                       [12, 18, 24]])



# Calculate the total number of products sold (sum of all elements)
total_products_sold = np.sum(sales_data)

# Calculate the average price of all products sold
average_price = total_products_sold / np.size(sales_data)

print("Average price of all products sold:", average_price)
