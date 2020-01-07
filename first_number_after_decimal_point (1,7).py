#Given a positive real number, print its first digit to the right of the decimal point.

#For example, on input
#56.8945
#output should be
#8

num = float(input())
round_num = num // 1
frac = num - round_num
print (str(frac)[2])
