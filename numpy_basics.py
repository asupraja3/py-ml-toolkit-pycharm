#Real-time usable numpy code snippets
import numpy as np
# Create a 1D array of integers from 0 to 9
array_1d = np.arange(10)
print("1D Array:", array_1d)
# Create a 2D array (matrix) of shape (3, 4) filled with zeros
print("2D Array:")
array_2d = np.zeros((3, 4))
print(array_2d)
# Create a 3D array (tensor) of shape (2, 3, 4) filled with ones
array_3d = np.ones((2, 3, 4))
print("3D Array:")
print(array_3d)
#Other useful numpy operations
# Create an array of evenly spaced values between 0 and 1 with 10 elements
array_even = np.linspace(0, 1, 10)
print("Evenly spaced array:", array_even)
# Create a random 2D array of shape (3, 3)
array_random = np.random.rand(3, 3)
print("Random 2D Array:")
print(array_random)
# Create a random integer array of shape (2, 3) with values between 0 and 10
array_random_int = np.random.randint(0, 10, (2, 3))
print("Random Integer Array:")
print(array_random_int)
# Reshape a 1D array into a 2D array
array_reshaped = array_1d.reshape((2, 5))  # Reshape to 2 rows and 5 columns
print("Reshaped Array:")
print(array_reshaped)
# Perform element-wise operations
array_sum = array_1d + 5  # Add 5 to each element
print("Element-wise addition (adding 5):", array_sum)
# Element-wise multiplication
array_product = array_1d * 2  # Multiply each element by 2
print("Element-wise multiplication (multiplying by 2):", array_product)
# Calculate the mean of the 1D array
array_mean = np.mean(array_1d)
print("Mean of 1D Array:", array_mean)
# Calculate the standard deviation of the 1D array
array_std = np.std(array_1d)
print("Standard Deviation of 1D Array:", array_std)
# Calculate the sum of all elements in the 1D array
array_sum_all = np.sum(array_1d)
print("Sum of all elements in 1D Array:", array_sum_all)
# Calculate the maximum and minimum values in the 1D array
array_max = np.max(array_1d)
array_min = np.min(array_1d)
print("Maximum value in 1D Array:", array_max)
print("Minimum value in 1D Array:", array_min)
# Transpose a 2D array
a = np.array([[1, 2, 3], [4, 5, 6]])
a_transposed = a.T
print("Transposed Array:", a_transposed)
# Concatenate two arrays along a specified axis
b = np.array([[7, 8, 9], [10, 11, 12]])
concatenated = np.concatenate((a, b), axis=0)  # Concatenate along rows
print("Concatenated Array:", concatenated)
# Stack two arrays along a new axis
stacked = np.stack((a, b), axis=0)  # Stack along a new axis
print("Stacked Array:", stacked)
# Stack two arrays along a new axis
# Create a mask to filter elements in the 1D array
print("Original Array:", array_1d)
mask = array_1d > 5  # Create a mask for elements greater than 5
filtered_array = array_1d[mask]  # Apply the mask to filter elements
print("Filtered Array (elements > 5):", filtered_array)
# most common numpy operations
