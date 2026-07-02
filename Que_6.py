import numpy as np

<<<<<<< HEAD
arr1 = np.random.randint(1,101,(5,5))
print(arr1)
print("Diagonal:")
print(np.diag(arr1))

print("Greater than 50:")
print(arr1[arr1 > 50])

arr1[arr1 < 30] = 0

print("Modified Array:")
print(arr1)
=======
v1 = np.array([2, 4, 6, 8])
v2 = np.array([1, 3, 5, 7])
print("vector 1",v1)
print("vector 2",v2)

print("Addition:",v1+v2)
print("Subtraction",v1-v2)
print("Multiplication",v1*v2)
print("Dot product",np.dot(v1,v2))
>>>>>>> 0fbd0d47662f02f06445dd11f5f3f9f690096b38
