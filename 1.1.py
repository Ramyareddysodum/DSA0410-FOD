import pandas as pd
from sklearn.impute import SimpleImputer

data = {
    'customer_id': [1, 2, 3, 4, 5],
    'product_id': [100, 101, 102, 103, 104],
    'order_date': ['2023-05-15', '2023-06-20', '2023-07-10', None, '2023-09-18'],
    'product_name': ['Product A', 'Product B', None, 'Product D', 'Product E'],
    'unit_price': [10.99, None, 15.99, 25.99, 30.49]
}
df = pd.DataFrame(data)

def handle_missing_values(df, strategy='mean'):
    try:
        imputer_numeric = SimpleImputer(strategy=strategy)
        imputer_non_numeric = SimpleImputer(strategy='most_frequent')

        # Separate numeric and non-numeric columns
        numeric_cols = df.select_dtypes(include='number').columns
        non_numeric_cols = df.select_dtypes(exclude='number').columns

        # Handle missing values for numeric columns
        df_numeric = pd.DataFrame(imputer_numeric.fit_transform(df[numeric_cols]), columns=numeric_cols)

        # Handle missing values for non-numeric columns
        df_non_numeric = pd.DataFrame(imputer_non_numeric.fit_transform(df[non_numeric_cols]), columns=non_numeric_cols)

        # Concatenate numeric and non-numeric columns
        df_imputed = pd.concat([df_numeric, df_non_numeric], axis=1)

        return df_imputed
    except Exception as e:
        print("Error occurred during missing value handling:", e)
        return None

# Example usage:
cleaned_df = handle_missing_values(df, strategy='most_frequent')  # Use 'most_frequent' strategy for non-numeric columns
print("Cleaned DataFrame:")
print(cleaned_df)
