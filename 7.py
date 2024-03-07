import pandas as pd

order_data = pd.DataFrame({
    'customer_id': [1, 2, 1, 3, 2, 3],
    'order_date': ['2024-01-01', '2024-01-02', '2024-01-03', '2024-01-04', '2024-01-05', '2024-01-06'],
    'product_name': ['A', 'B', 'A', 'C', 'B', 'A'],
    'order_quantity': [2, 3, 1, 2, 4, 1]
})

# 1. Total number of orders made by each customer
total_orders_per_customer = order_data.groupby('customer_id').size()

print("Total number of orders made by each customer:")
print(total_orders_per_customer)
print()

# 2. Average order quantity for each product
average_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()

print("Average order quantity for each product:")
print(average_order_quantity_per_product)
print()

# 3. Earliest and latest order dates in the dataset
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()

print("Earliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
