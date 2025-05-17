import numpy as np

dict_1 = {}
value_1 = []

name = input("Enter the student name: ")
sub = int(input("Enter number of subjects: "))

for mark in range(sub):
    key, value = input("Enter the subject name and marks by giving space: ").split()
    value = int(value)  # Convert value to integer
    value_1.append(value)
    dict_1[key] = value

# Convert to NumPy array
marks_array = np.array(value_1)

# Find max and min subject
subjects = list(dict_1.keys())
marks = list(dict_1.values())

max_index = np.argmax(marks)
min_index = np.argmin(marks)

print(f"\n{name} got maximum marks in {subjects[max_index]}: {marks[max_index]}")
print(f"{name} got minimum marks in {subjects[min_index]}: {marks[min_index]}")
print(f"{name}'s average marks: {np.mean(marks_array)}")
print(f"{name}'s total marks: {np.sum(marks_array)}")
