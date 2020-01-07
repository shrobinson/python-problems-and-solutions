#Implement a function my_max(lst) that given a list of integer numbers lst returns its maximum.

#Do not use the standard function max or a loop of any kind. Instead implement my_max recursively relying on the following principle:
#- if list contains just one element n then its maximum is equal n
#- othewise,  the maximum is either the first value in the list or the maximum of the rest of the list, whichever is larger 

#For example, the result of
#print(my_max([3,2,5]))
#must be
#5

def my_max(lst):
  if len(lst) == 1:
    return lst[0]
  else:
     maxi = my_max(lst[1:])
     return maxi if maxi > lst[0] else lst[0]
