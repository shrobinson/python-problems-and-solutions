#Given a list of numbers, find and print all the elements that are greater than the previous element. 

#For example, on input
#10 6 11 13 10 10 23
#output must be
#11 13 23

s = input()

num_strs = s.split()

nums = []
for num_str in num_strs:
  nums.append(int(num_str))
  
for i in range(0, len(nums)-1):
  if nums[i+1] > nums[i]:
    print(nums[i+1], end = " ")
