#Implement a function max_three(num1, num2, num3) that returns the maximal of three numbers num1, num2, num3.

#Note. You must use functions in this excercise. Do not change the name of the required function.

#For example, the result of 
#n = max_three(4,2,5)
#print(n)
#must be
#5

def max_three(num1, num2, num3):
  if num2 >= num1 and num2 >= num3:
    return num2
  elif num3 >= num2 and num3 >= num1:
    return num3
  else:
    return num1

n = max_three(4,2,5)
print(n)
