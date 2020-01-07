#Given a list of numbers, print all elements that are an even number in the original order.

#For example, on input:
#3 2 6 55 7 13 10
#output must be
#2 6 10

list_info = input()
list_info = [list_info]
new_list = []
even_list = []

for i in list_info:
  new_list.extend(i.split(" "))
  new_list = [int(i) for i in new_list]

for i in new_list:
  if i % 2 == 0:
    even_list.append(i)
print(*even_list)
