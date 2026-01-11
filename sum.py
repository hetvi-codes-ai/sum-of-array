import numpy as np

n = input("Enter numbers separated by space: ")

na = np.array(n.split(), dtype=int)

sum = np.sum(na)

print("Array elements:", na)
print("Sum of elements:", sum)
