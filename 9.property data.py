import pandas as pd
data = {
    'property_id': [101, 102, 103, 104, 105],
    'location': ['City A', 'City B', 'City A', 'City C', 'City B'],
    'bedrooms': [3, 5, 2, 4, 6],
    'area_sqft': [1500, 2000, 1200, 1800, 2500],
    'listing_price': [300000, 450000, 250000, 400000, 500000]
}
property_data = pd.DataFrame(data)
avg_price_per_location = property_data.groupby('location')['listing_price'].mean()
properties_with_more_than_4_bedrooms = property_data[property_data['bedrooms'] > 4].shape[0]
largest_property = property_data.loc[property_data['area_sqft'].idxmax()]
print("Average listing price in each location:")
print(avg_price_per_location)
print("\nNumber of properties with more than four bedrooms:", properties_with_more_than_4_bedrooms)
print("\nProperty with the largest area:")
print(largest_property)
