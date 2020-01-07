#A sequence consists of integer numbers and ends with the number 0. Determine how many elements of this sequence are greater than their neighbours above. 

#For example, on input
#3
#2
#3
#1
#4
#4
#3
#0
#output must be
#2

count = 0
value = int(input())
value2 = int(input())
while value2 != 0:
  previous = value
  value = value2
  if value2 > previous:
    count = count + 1
  else:
    count = count
  value2 = int(input())
print(count)
