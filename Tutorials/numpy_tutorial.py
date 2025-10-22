import numpy as np

# a_mul = np.array([[1,2,3], [4,5,6], [7,8,9]], dtype="<U7")
# a_mul.reshape((9,)) # 1 row
# a_mul.reshape((9,1)) # 1 column
# a_mul.reshape((3, 3, 1))
# a_mul.resize((9,1)) # Mutates the original matrix
# a_mul.flatten() # Returns flattened copy of original
# a_mul.flat
# a_mul.ravel() # Mutating original to flatten
# print(a_mul.shape, a_mul.ndim, a_mul.size, a_mul.dtype) # (3, 3)

# a = np.full((2, 3, 4), 9)
# b = np.zeros((2, 5, 3))
# c = np.empty((5, 5, 5)) # Allocates memory

# x_values = np.arange(0, 1001, 5)
# y_values = np.linspace(0, 1000, 2)
# print(a, b, c)
# print(np.nan, np.inf)

# print(np.isnan(np.sqrt(-1)), np.isinf(np.array([10]) / 0))

# l1 = [1, 2, 3, 4, 5] * 2
# l2 = [6, 7, 8, 9, 0]

# a1 = np.array(l1[len(l1) // 2]) * 2
# a2 = np.array(l2)

# a = np.array([1, 2, 3])
# np.append(a, [7, 8, 9]) # Does not overwrite the variable by default
# a = np.insert(a, 3, [4, 5, 6])
# np.delete(a, 1, 1) # Deletes Arg2 based on if Arg3 is 0 (row) or 1 (column), etc. 

# a1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
# a2 = np.array([[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]])
# a = np.concatenate((a1, a2), axis = 1) # 0 - Row, 1 - Column, basically x/y/z/etc. axes
# np.vstack((a1, a2)) # Like concatenate with axis = 0
# np.hstack((a1, a2)) # Like concatenate with axis = 1
# np.stack((a1, a2)) # Adds a new dimension
# np.split(a, 2, axis = 0) # Creates 2 rows
# np.split(a, 5, axis = 1) # Splits each row into Arg2 amount of columns

# a.transpose() 
# a.T
# a.swapaxes(0, 1) # Good for only swapping specific axes

# a.min(), a.max(), a.mean(), a.std(), a.sum(), np.median(a)

# numbers = np.random.randint(90, 100, size=(2, 3, 4))
# numbers = np.random.binomial(10, p=0.5, size=(5, 10))
# numbers = np.random.normal(loc=170, scale=15, size=(5, 10))

np.save("myarray.npy", a) # Saves matrix as npy file
a = np.load("myarray.npy")
np.save("myarray.csv", a, delimiter=" ")
a = np.loadtxt("myarray.csv", delimiter=" ")