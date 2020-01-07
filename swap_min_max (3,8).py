#Given a list of unique numbers, swap the minimal and maximal elements of this list. Print the resulting list. 

#For example, on input:
#5 7 3 2 1 6
#output must be
#5 1 3 2 7 6

s = input()

num_strs = s.split()

nums = []
for num_str in num_strs:
  nums.append(int(num_str))

max_num = max(nums)
min_num = min(nums)

new_list = []

for i in range (0, len(nums)):
  if nums[i] == max_num:
    new_list.append(min_num)
  elif nums[i] == min_num:
    new_list.append(max_num)
  else:
    new_list.append(nums[i])

print(*new_list)
