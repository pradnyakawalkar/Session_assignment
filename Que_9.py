import numpy as np

<<<<<<< HEAD
<<<<<<< HEAD
arr3 = np.random.randn(6,6)
print(arr3)

print("shape",arr3.shape)
print("minimum",arr3.argmin())
print("maximum",arr3.argmax())
print("Top Left 3x3:")
print(arr3[:3, :3])


print("Modified Array:")
print(arr3)
print("Mean =", arr3.mean())
=======
=======
>>>>>>> aa0dcaed7c9663c115c1d8e353332f775de9aae7
a = np.random.randint(1,51,20)

b = a.reshape(4,5)

print("Matrix")
print(b)

print("\n sum =",b.sum())
print("mean =",b.mean())
print("Standard Deviation =",b.std())
print("\n Maximum value in each row")
print(b.max(axis=1))
<<<<<<< HEAD
>>>>>>> 0fbd0d47662f02f06445dd11f5f3f9f690096b38
=======
>>>>>>> aa0dcaed7c9663c115c1d8e353332f775de9aae7
