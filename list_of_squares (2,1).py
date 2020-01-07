#For a given integer N, print all the squares of integer numbers where the square is less than or equal to N, in ascending order.

#For example, on input
#10
#output must be
#1 4 9

n = int(input())
for i in range (1, n+1):
  if i * i <= n:
    print(i * i)
print()
 
