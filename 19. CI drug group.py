import numpy as np
import scipy.stats as stats
drug_group = [10, 12, 8, 15, 9, 11, 13, 14, 7, 10, 16, 9, 12, 8, 15, 11, 10, 12, 14, 9, 8, 7, 12, 13, 14]
placebo_group = [5, 6, 5, 7, 4, 6, 5, 7, 4, 5, 6, 4, 5, 7, 4, 6, 5, 6, 5, 7, 4, 5, 6, 4, 5]
def confidence_interval(data, confidence=0.95):
    n = len(data)
    mean = np.mean(data)
    std_err = stats.sem(data) 
    z_score = stats.norm.ppf((1 + confidence) / 2)
    margin_of_error = z_score * std_err
    return mean - margin_of_error, mean + margin_of_error
drug_ci = confidence_interval(drug_group)
print(f"95% Confidence Interval for Drug Group: {drug_ci}")
placebo_ci = confidence_interval(placebo_group)
print(f"95% Confidence Interval for Placebo Group: {placebo_ci}")
