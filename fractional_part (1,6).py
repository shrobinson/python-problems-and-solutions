#Given a positive real number, print its fractional part. 

#For example, on input
#34.056
#the output should be
#0.056

#Note. Due to imprecisions of float arithmetic, you may get 0.05599999 as the result in the example above, which is "almost" correct. Use round operation to get the correct output as in the example below:

#n = 0.05599999
#rounded_n = round(n, 3)  #rounding to 3 digits after .
                         #rounded_n will be 0.056

num = float(input())
round_num = num // 1
frac = num - round_num
round_frac = round(frac,3)
print(round_frac)
