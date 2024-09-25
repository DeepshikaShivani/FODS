import pandas as pd
data = pd.read_csv('temperature_data.csv')
print(data.head())
mean_temperatures = data.groupby('City')['Temperature'].mean().reset_index()
mean_temperatures.rename(columns={'Temperature': 'Mean_Temperature'}, inplace=True)
std_temperatures = data.groupby('City')['Temperature'].std().reset_index()
std_temperatures.rename(columns={'Temperature': 'Std_Deviation'}, inplace=True)
stats = pd.merge(mean_temperatures, std_temperatures, on='City')
data['Temperature_Range'] = data.groupby('City')['Temperature'].transform(lambda x: x.max() - x.min())
city_highest_range = data.groupby('City')['Temperature_Range'].max().reset_index()
city_highest_range = city_highest_range.loc[city_highest_range['Temperature_Range'].idxmax()]
most_consistent_city = stats.loc[stats['Std_Deviation'].idxmin()]
print("\nMean and Standard Deviation of Temperatures for Each City:")
print(stats)
print("\nCity with the Highest Temperature Range:")
print(city_highest_range)
print("\nCity with the Most Consistent Temperature (Lowest Standard Deviation):")
print(most_consistent_city)
