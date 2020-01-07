#Determine the sum of all elements in the sequence, ending with the number 0. 

#For example, on input
#1
#2
#3
#0
#output must be
#6

n = int(input())
sum = 0
while n > 0:
  sum = sum + n
  n= int(input())
print(sum)
