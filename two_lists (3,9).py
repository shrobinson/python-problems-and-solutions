#Given two lists of numbers, print the numbers that are in the fist list but are not in the second. Print those numbers in the ascending order. (You can assume that the numbers in each of the two lists do not repeat.)

#For example, on input
#20 4 45 6 10
#9 10 6 3
#output must be
#4 20 45

s = input()
s2 = input()

num_strs = s.split()
num_strs2 = s2.split()

nums = []
for num_str in num_strs:
  nums.append(int(num_str))
  
nums2 = []
for num_str in num_strs2:
  nums2.append(int(num_str))

nums_set = set(nums)
nums2_set = set(nums2)

distinct = nums_set-nums2_set
s3 = list(distinct)
s3.sort()

print(*s3)
  
