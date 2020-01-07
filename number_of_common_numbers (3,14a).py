#Given two lists of numbers, count how many unique numbers occur in both of them. 

#Hint. Use sets to solve this problem quickly.

#For example, on input
#5 3 3 10 40
#40 3 40 1 2
#output must be
#2

s = input()
r = input()

num_strs = s.split()
num_strs2 = r.split()

set1 = set(num_strs)
set2 = set(num_strs2)

unique = set1.intersection(set2)

count = len(unique)
print(count)
