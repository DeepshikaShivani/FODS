import numpy as np
import pandas as pd
from scipy import stats
data = pd.read_csv('rare_elements.csv')
concentration_data = data['concentration'].values
def calculate_confidence_interval(data, confidence_level, precision):
    sample_mean = np.mean(data)
    standard_error = np.std(data, ddof=1) / np.sqrt(len(data))
    z_value = stats.norm.ppf((1 + confidence_level) / 2)
    margin_of_error = z_value * standard_error
    lower_bound = sample_mean - margin_of_error
    upper_bound = sample_mean + margin_of_error
    return sample_mean, lower_bound, upper_bound
sample_size = int(input("Enter the sample size: "))
confidence_level = float(input("Enter the confidence level (e.g., 0.95 for 95%): "))
precision = float(input("Enter the desired level of precision: "))
if sample_size <= len(concentration_data):
    sample = np.random.choice(concentration_data, sample_size, replace=False)
else:
    print("Sample size exceeds the available data. Please enter a smaller sample size.")
    exit()
mean, lower, upper = calculate_confidence_interval(sample, confidence_level, precision)
print(f"Sample Mean: {mean}")
print(f"Confidence Interval: ({lower}, {upper}) with {confidence_level * 100}% confidence level")
