#Real-time usable numpy code snippets
import numpy as np
# Create a 1D array of integers from 0 to 9
#Parameters explained:
# np.arange(start, stop, step) - Creates an array with evenly spaced values within a given range.
# start: value is inclusive, and stop: value is exclusive.
# step: value determines the spacing between the values.
array_1d = np.arange(10)
print("1D Array:", array_1d)
# Create a 2D array (matrix) of shape (3, 4) filled with zeros
print("2D Array:")
array_2d = np.zeros((3, 4))
#Parameters explained:
# np.zeros(shape) - Creates an array filled with zeros.
# shape: parameter specifies the dimensions of the array.
print(array_2d)
# Create a 3D array (tensor) of shape (2, 3, 4) filled with ones
#Parameters explained:
# np.ones(shape) - Creates an array filled with ones.
# shape: parameter specifies the dimensions of the array.
array_3d = np.ones((2, 3, 4))
print("3D Array:")
print(array_3d)
#Other useful numpy operations
# Create an array of evenly spaced values between 0 and 1 with 10 elements
#Parameters explained:
# np.linspace(start, stop, num) - Creates an array of evenly spaced values over a specified range.
# start: value is inclusive, stop: value is inclusive, num: number of elements to generate.
array_even = np.linspace(0, 1, 10)
#output: [0.         0.11111111 0.22222222 0.33333333 0.44444444 0.55555556 0.66666667 0.77777778 0.88888889 1.        ]
print("Evenly spaced array:", array_even)
# Create a random 2D array of shape (3, 3)
#Parameters explained:
# np.random.rand(d0, d1, ..., dn) - Creates an array of the given shape filled with random values
# from a uniform distribution over [0.0, 1.0).
# d0, d1, ..., dn: dimensions of the array.
array_random = np.random.rand(3, 3)
print("Random 2D Array:")
print(array_random)
# Create a random integer array of shape (2, 3) with values between 0 and 10
##Parameters explained:
# np.random.randint(low, high, size) - Creates an array of random integers from low (inclusive) to high (exclusive).
# low: lower bound (inclusive), high: upper bound (exclusive), size: shape of the output array.
array_random_int = np.random.randint(0, 10, (2, 3))
print("Random Integer Array:")
print(array_random_int)
# Reshape a 1D array into a 2D array
#Parameters explained:
# np.reshape(array, new_shape) - Reshapes an array to a new shape without changing its data.
# new_shape: tuple specifying the new shape of the array. array: the input array to be reshaped.
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
#Parameters explained:
# np.mean(array) - Calculates the mean (average) of the elements in the array.
# array: the input array for which the mean is calculated.
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
#Parameters explained:
# np.concatenate((array1, array2), axis) - Concatenates two or more arrays along a specified axis.
# array1, array2: input arrays to be concatenated, axis: axis along which the arrays are concatenated.
b = np.array([[7, 8, 9], [10, 11, 12]])
concatenated = np.concatenate((a, b), axis=0)  # Concatenate along rows
print("Concatenated Array:", concatenated)
# Stack two arrays along a new axis
#Parameters explained:
# np.stack((array1, array2), axis) - Stacks two or more arrays along a new axis.
# array1, array2: input arrays to be stacked, axis: axis along which the arrays are stacked.
stacked = np.stack((a, b), axis=0)  # Stack along a new axis
print("Stacked Array:", stacked)
# Stack two arrays along a new axis
# Create a mask to filter elements in the 1D array
print("Original Array:", array_1d)
mask = array_1d > 5  # Create a mask for elements greater than 5
filtered_array = array_1d[mask]  # Apply the mask to filter elements
print("Filtered Array (elements > 5):", filtered_array)
# most common numpy operations
