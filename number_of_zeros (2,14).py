#Given N numbers: the first number in the input is N, after that N integers are given. Count the number of zeros among the given integers and print it. You need to count the number of numbers that are equal to zero, not the number of zero digits.

#Recommendation. Use for loops.

#For example, on input
#4
#1
#0
#3
#0
#output must be
#2

sum = 0 
N = int(input())
for i in range(0, N):
  n = int(input())
  if n == 0:
    sum = sum + 1
print(sum)
 
 
