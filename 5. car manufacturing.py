import numpy as np
fuel_efficiency = np.array([25, 30, 35, 40, 32]) 
average_efficiency = np.mean(fuel_efficiency)
model1_efficiency = fuel_efficiency[0] 
model2_efficiency = fuel_efficiency[-1] 
percentage_improvement = ((model2_efficiency - model1_efficiency) / model1_efficiency) * 100
print(f"Average fuel efficiency: {average_efficiency:.2f} miles per gallon")
print(f"Percentage improvement in fuel efficiency from model 1 to model 2: {percentage_improvement:.2f}%")
