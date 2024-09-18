import numpy as np
student_scores = np.array([
    [85, 90, 78, 92], 
    [88, 76, 85, 80],
    [70, 85, 89, 90],
    [92, 88, 91, 85]
])
subject_averages = np.mean(student_scores, axis=0)
highest_avg_subject_index = np.argmax(subject_averages)
subject_names = ["Math", "Science", "English", "History"]
print(f"Average scores for each subject: {subject_averages}")
print(f"Subject with the highest average score: {subject_names[highest_avg_subject_index]}")
