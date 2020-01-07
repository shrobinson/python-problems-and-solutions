#A sequence consists of integer numbers and ends with the number 0. Determine the largest element of the sequence. 

#For example, on input
#4
#7
#2
#0
#output must be
#7

n = int(input())
max = 0
while n != 0:
  if n > max:
    max = n
  n = int(input())
print(max)
    
  
