# Write a Python program to sum of three given integers. However, if two values are equal sum will be zero.

def sum_thrice(x, y, z):
 
     sum = x + y + z
 
     if x == y == z:
      sum = sum * 3
     return sum
 
print(sum_thrice(1, 2, 3))
print(sum_thrice(3, 3, 3))
