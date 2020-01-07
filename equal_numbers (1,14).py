#Given three integers, determine how many of them are equal to each other. The program must print one of these numbers: 3 (if all are the same), 2 (if two of them are equal to each other and the third is different) or 0 (if all numbers are different). 

#For example, on input
#4
#5
#4
#output must be
#2

num1 = int(input())
num2 = int(input())
num3 = int(input())

if num1 == num2 and num2 == num3:
  print(3)
elif num1 == num2 or num2 == num3 or num1 == num3:
  print(2)
else:
  print(0)
