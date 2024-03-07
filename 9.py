import pandas as pd
df = pd.read_csv("C:\\Users\\91944\\Desktop\\property.csv")
average_price_by_location = df.groupby('location')['listing_price'].mean()
print(average_price_by_location)
properties_more_than_four_bedrooms = df[df['bedrooms'] > 4]
num_properties_more_than_four_bedrooms = len(properties_more_than_four_bedrooms)
print("Number of properties with more than four bedrooms:", num_properties_more_than_four_bedrooms)
property_with_largest_area = df.loc[df['area'].idxmax()]
print("Property with the largest area:")
print(property_with_largest_area)
