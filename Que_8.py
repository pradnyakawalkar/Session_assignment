import numpy as np

<<<<<<< HEAD
A = np.array([[1,2,3],[4,5,6],[7,8,9]])
B = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(A)
print("\n")
print(B)
print("Element-wise multiplication:", A*B)
print("Matrix multiplication:",np.dot(A,B))

# Difference:
# * multiplies corresponding elements.
# @ performs actual matrix multiplication.
=======
a = np.random.randint(1,101,(4,4))

print("Matrix")
print(a)

print("\nShape =", a.shape)
print("Dimension =", a.ndim)
print("Size =", a.size)
print("Data Type =", a.dtype)
print("Minimum =", a.min())
print("Maximum =", a.max())
>>>>>>> 0fbd0d47662f02f06445dd11f5f3f9f690096b38
