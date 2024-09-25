import pandas as pd
import numpy as np
from scipy import stats
data = pd.read_csv('customer_reviews.csv')df
ratings = data['rating']
mean_rating = ratings.mean()
standard_error = stats.sem(ratings)
confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95%): "))
z_value = stats.norm.ppf((1 + confidence_level) / 2)
margin_of_error = z_value * standard_error
lower_bound = mean_rating - margin_of_error
upper_bound = mean_rating + margin_of_error
print(f"Sample Mean Rating: {mean_rating:.2f}")
print(f"{confidence_level * 100}% Confidence Interval: ({lower_bound:.2f}, {upper_bound:.2f})")
