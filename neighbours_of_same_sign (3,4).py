#Given a list of numbers, find and print the first adjacent elements which have the same sign. If there is no such pair, leave the output blank. 

#For example, on input
#-1 2 -3 -4 -5 1 2
#output must be
#-3 -4

s = input()

num_strs = s.split()

nums = []
for num_str in num_strs:
  nums.append(int(num_str))
  
for i in range(0, len(nums)-1):
  if nums[i+1] >= 0 and nums[i] >= 0 or nums[i+1] < 0 and nums[i] < 0:
    print(nums[i],nums[i+1], end = " ")
    break
