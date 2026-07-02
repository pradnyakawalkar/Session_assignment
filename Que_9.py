import numpy as np

a = np.random.randint(1,51,20)

b = a.reshape(4,5)

print("Matrix")
print(b)

print("\n sum =",b.sum())
print("mean =",b.mean())
print("Standard Deviation =",b.std())
print("\n Maximum value in each row")
print(b.max(axis=1))
