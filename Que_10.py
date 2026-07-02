import numpy as np
<<<<<<< HEAD
<<<<<<< HEAD

marks = np.random.randint(30,101,(10,5))
print(marks)

total= marks.sum(axis = 1)
print("\n",total)

average = marks.mean(axis = 1)
print("\n",average)

lowest = total.argmin()
highest = total.argmax()
print("\n",highest)
print("\n",lowest)

print("\n","mean =",marks.mean())
print("\n","Standard deviation=",marks.std())

top3 = total.argsort()[-3:]

print("\nTop 3 Students Index:")
print(top3)

print("\nMarks of Top 3 Students:")
print(marks[top3])


# Comments:
# sum(axis=1) calculates total marks.
# mean(axis=1) calculates average marks.
# argmax() and argmin() find highest and lowest scorers.
# argsort() helps find top students.
=======
=======
>>>>>>> aa0dcaed7c9663c115c1d8e353332f775de9aae7
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
<<<<<<< HEAD
    print("Invalid Input")
>>>>>>> 0fbd0d47662f02f06445dd11f5f3f9f690096b38
=======
    print("Invalid Input")
>>>>>>> aa0dcaed7c9663c115c1d8e353332f775de9aae7
