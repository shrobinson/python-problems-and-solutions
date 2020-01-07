#For a given integer N, find the greatest integer x where 2 to the power of x is less than or equal to N. Print the exponent value x and the result of 2 to the power of x.

#For example, on input
#20
#output must be
#4 16

N = int(input())
x = 1
result = 2
new_result = 0
old_result = 0
while new_result <= N:
    old_result = result
    result = result * 2
    new_result = result
    x += 1
print((x-1), old_result)
