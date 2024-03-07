#1.5
import pandas as pd
integrated_df = pd.DataFrame({
        'order_id': [1, 2, 3, 4, 5],
        'product_id': [101, 102, None, 104, 105],
        'customer_id': [201, 202, None, None, 205],
        'quantity': [2, 1, 3, 2, 1]
    })
resultant_df=integrated_df.dropna()
print(resultant_df)
check_data_quality(integrated_df)
