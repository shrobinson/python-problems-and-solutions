#For the given integer X print 1 if it's positive, -1 if it's negative, or 0 if it's equal to zero. 

#For example, on input
#-13
#output should be
#-1

num = int(input())
if num > 0:
  print(1)
elif num < 0:
  print(-1)
else:
  print(0)
