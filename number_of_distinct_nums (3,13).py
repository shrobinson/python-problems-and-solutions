#Implement a function distinct_nums(L) that, given a list of integers, L, returns how many distinct numbers there are in L.

#Note. This task can be solved very quickly using sets.

#For example, the result of
#print(distinct_nums([5,3,2,3,2,4]))
#must be
#4

#implement the required function
def distinct_nums(L):
  unique_nums = set(L)
  unique_count = len(unique_nums)
  return(unique_count)
