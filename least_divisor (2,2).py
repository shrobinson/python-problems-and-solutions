#Given an integer not less than 2. Print its smallest integer divisor greater than 1. 

#For example, on input
#9
#output must be
#3

n = int(input())
divisor = 2 
small_div = 0
while n % divisor!= 0:
  if n % divisor == 0:
    small_div = divisor
  else:
    divisor += 1
print(divisor)
