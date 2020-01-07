#A flower costs A pounds and B pence. Determine, how many pounds and pence should one pay for N flowers. A program gets three numbers: A, B, N. It should print two numbers: total cost in pounds and pence. 

#For example, on input 
#1
#50
#3
#output should be
#4
#50

A = int(input())
B = int(input())
N = int(input())

pounds_to_penny = A * 100
pounds_amount = pounds_to_penny * N
pence = pounds_amount + (B * N)
total_pounds = pence // 100
total_pence = (pence % 100)

print(total_pounds)
print(total_pence)
