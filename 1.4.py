import pandas as pd
data = pd.DataFrame({
    'customer_id': [1, 2, 3, None],
    'order_id': [101, 102, None, 104],
    'product_id': [201, 202, 203, 203],
    'product_name': ['Product A', 'Product B', 'Product C', 'Product C'],
    'price': [10.0, 20.0, 30.0, 30.0],
    'quantity': [1, 2, None, 4],
    'review_score': [5, 4, 5, None]
})
numeric_columns = ['customer_id', 'order_id', 'product_id', 'price', 'quantity', 'review_score']
data[numeric_columns] = data[numeric_columns].fillna(data[numeric_columns].mean())
categorical_columns = ['product_name']
data[categorical_columns] = data[categorical_columns].fillna(data[categorical_columns].mode().iloc[0])
print("Cleaned Dataset:")
print(data)
