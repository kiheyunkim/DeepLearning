import numpy as np
arr = np.array([1, 2, 3, 4])

print(arr)
print(np.ndim(arr))
print(arr.shape)
print(arr.shape[0])

arr2 = np.array([[1, 2], [3, 4], [5, 6]])
print(arr2)
print(np.ndim(arr2))
print(arr2.shape)

arr3 = np.array([[1, 2], [3, 4]])
print(arr3.shape)

arr4 = np.array([[5, 6], [7, 8]])
print(arr4.shape)
print(np.dot(arr3, arr4))