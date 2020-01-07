#Read a single line of text containing a list of numbers (separated by space).  Print all the list elements with an even index number. (i.e. A[0], A[2], A[4], ...) 

#Hint. Use s.split(), where s is a string, to obtain a list of strings resulting from splitting s using space as separator

#For example, on input
#13 4 23 4 5 6
#output must be
#13 23 5

list_info = input()
list_info = [list_info]
new_list = []

for i in list_info:
  new_list.extend(i.split(" "))
  
even_list = new_list[0::2]
print(*even_list)
