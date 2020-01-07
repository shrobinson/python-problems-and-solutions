#Given two integers A and B. Print all numbers from A to B inclusively, in ascending order, if A < B, or in descending order, if A ≥ B. 

#Recommendation. Use for loops.

#For example, on input
#4
#2
#output must be
#4 3 2

A = int(input())
B = int(input())
if A < B:
  for i in range(A, B+1):
    print(i)
else:
  for i in range(A, B-1,-1):
    print(i)
print()
