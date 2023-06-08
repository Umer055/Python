from math import sqrt

def getPentagonalNumber(n):

   return int((3 * n * n - n) / 2)

for p in range(1, 100, 10):

   for x in range(p, p+10):

       print(getPentagonalNumber(x), end=" ")

   print()
   