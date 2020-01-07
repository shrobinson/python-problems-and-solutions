#N numbers are given in the input. Read them and print their sum.

#The first line of input contains the integer N, which is the number of integers to follow. Each of the next N lines contains one integer. Print the sum of these N integers.

#Recommendation. Use for loops.

#For example, on input
#4
#7
#10
#15
#3
#output must be
#35

sum = 0 
N = int(input())
for i in range(0, N):
  n = int(input())
  sum = sum + n
print(sum)
 
