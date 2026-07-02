import numpy as np
try:
     n = int(input("Enter how mant numbers:"))
     arr = np.random.randint(10,101,n)
     print("\n Generated array")
     print(arr)
     print("\nMean =", np.mean(arr))
     print("\nMedian =", np.median(arr))
     print("\nStandard Deviation =", np.std(arr))
     print("\nMinimum =", np.min(arr))
     print("\nMaximum =", np.max(arr))

     if n % 2 == 0:
          n == arr.reshape(2,n//2)
          print("\n2D Array")
          print(n)

          print("\nRow-wise Sum")
          print(n.sum(axis=1))
     else:
          print("\nCannot reshape into 2D array")

except ValueError:
    print("Invalid Input")