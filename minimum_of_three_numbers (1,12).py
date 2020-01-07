#Given three integer numbers, determine their minimum

#For example, on input
#4
#2
#7
#the output should be
#2

num = int(input())
num2 = int(input())
num3 = int(input())

if num2 >= num and num3 >= num:
  min_num = num
elif num3 >= num2:
  min_num = num2
else:
  min_num = num3
print(min_num)
