#Given a string that may or may not contain a letter of interest. Print the index location of the first and last appearance of f. If the letter f occurs only once, then output its index. If the letter f does not occur, then print -1. 

#For example, on input
#fearful
#output must be
#0 4

inputStr = input()

exist = inputStr.find('f')
if exist == -1:
  print(-1)

new_list = []

if exist != -1:
  for i in range(len(inputStr)):
    if inputStr[i] == 'f':
      new_list.append(i)
      new_list.sort()

if len(new_list) > 1:
  print(min(new_list), max(new_list))
else:
  print(*new_list)
