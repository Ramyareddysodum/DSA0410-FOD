import pandas as pd
order_data = {
     'customer_id': [1, 2, 3, 4, 5],
    'product_id': [100, 101, 102, 103, 104],
    'order_date': ['2023-05-15', '2023-06-20', '2023-07-10', '2023-08-05', '2023-09-18']
}
products_data = {
    'product_id': [100, 101, 102, 103, 104],
    'product_name': ['Product A', 'Product B', 'Product C', 'Product D', 'Product E'],
    'unit_price': [10.99, 20.49, 15.99, 25.99, 30.49]
}

df_orders = pd.DataFrame(order_data)
df_products = pd.DataFrame(products_data)
def integrate_datasets(df_orders,df_products):
    try:
        integrated_df = pd.merge(df_orders,df_products, on='product_id',how = 'left')
        return integrated_df
    except Exception as e:
        print("Error occured during data integration:",e)
        return None
integrated = integrate_datasets(df_orders,df_products)
print("integrated datasets")
print(integrated)
