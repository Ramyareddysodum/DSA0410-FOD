import pandas as pd
order_data = pd.DataFrame({
    'customer_id': [1, 2, 1, 3, 2],
    'order_date': ['2023-01-01', '2023-01-02', '2023-01-01', '2023-01-03', '2023-01-02'],
    'product_name': ['A', 'B', 'A', 'C', 'B'],
    'order_quantity': [2, 3, 1, 2, 4]
})
total_orders_per_customer = order_data.groupby('customer_id').size()
average_order_quantity_per_product = order_data.groupby('product_name')['order_quantity'].mean()
earliest_order_date = order_data['order_date'].min()
latest_order_date = order_data['order_date'].max()
print("Total number of orders made by each customer:")
print(total_orders_per_customer)
print("\nAverage order quantity for each product:")
print(average_order_quantity_per_product)
print("\nEarliest order date:", earliest_order_date)
print("Latest order date:", latest_order_date)
