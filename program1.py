


import numpy as np
array_from_list = np.array([1, 2, 3, 4, 5])
print("Array from list:", array_from_list)

array_with_range = np.arange(10)
print("Array with range:", array_with_range)

zeros_array = np.zeros((3, 3))
print("Array of zeros:\n", zeros_array)

ones_array = np.ones((2, 5))
print("Array of ones:\n", ones_array)

import numpy as np
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
add_result = np.add(a, b)
print("Addition:", add_result)
sub_result = np.subtract(a, b)
print("Subtraction:", sub_result)
mul_result = np.multiply(a, b)
print("Multiplication:", mul_result)
div_result = np.divide(a, b)
print("Division:", div_result)



import numpy as np
array = np.arange(12)
print("Original array:", array)
reshaped_array = array.reshape((3, 4))
print("Reshaped to 3x4:\n", reshaped_array)
reshaped_array_3d = array.reshape((2, 3, 2))
print("Reshaped to 2x3x2:\n", reshaped_array_3d)

import numpy as np
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("2D Array:\n", array_2d)
element = array_2d[1, 2]
print("Element at (1, 2):", element)

subarray = array_2d[1:3, 0:2]
print("Sliced subarray:\n", subarray)
column = array_2d[:, 1]
print("Column 1:", column)

import numpy as np
array = np.array([1,2,3,4,5,6,7,8,9,10])
mean =np.mean(array)
print("Mean:",mean)

median =np.median(array)
print("Median:",median)

std_dev = np.std(array)
print("Standard Deviation:",std_dev)

min_val =np.min(array)
max_val = np.max(array)
print("Minimum value:",min_val)
print("Maximum value:",max_val)