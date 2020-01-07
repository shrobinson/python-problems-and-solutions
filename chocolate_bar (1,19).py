#Chocolate bar has the form of a rectangle divided into n×m portions. Chocolate bar can be split into two rectangular parts by breaking it along a selected straight line on its pattern. 

#Determine whether it is possible to split it so that one of the parts will have exactly k squares.
#The program reads three integers: n, m, and k. It should print YES or NO.

#For example, on input
#2
#10
#7
#output must be 
#NO

n = int(input())
m = int(input())
k = int(input())

if n > 1 and m > 1:
  if n*m / 2 <= k:
    print("YES")
  else:
    print("NO")
elif n == 1 or m == 1:
  if n*m > k:
    print("YES")
  else:
    print("NO")
else:
    print("NO")

