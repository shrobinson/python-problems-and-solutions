#Given two integers A and B (A ≤ B). Print all numbers from A to B inclusively. 

#Recommendation. Use for loops.

#For example, on input
#4
#7
#output must be
#4 5 6 7

a = int(input())
b = int(input())
for i in range(a,b+1):
  print(i, end = " ")
