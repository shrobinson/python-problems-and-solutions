#Given a three-digit number, find the sum of its digits.

#For example, on input 
#163
#the output should be 
#10

n = int(input())
last_dig = n % 10
second_last_dig = (n // 10) % 10
first_dig = n // 100
print(first_dig + second_last_dig + last_dig)
