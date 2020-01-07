#Determine the average a of all elements of the sequence ending with the number 0. 

#Note. Print only the integer part of a (ignore fractional part).

#For example, on input
#1
#2
#4
#0
#output must be
#2

n = int(input())
sum = 0
count = 0
while n != 0:
  sum = sum + n
  count += 1
  a = int(sum / count)
  n = int(input())
print(a)
