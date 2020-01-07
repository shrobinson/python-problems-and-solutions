#Given a list of numbers, swap adjacent items in pairs (A[0] with A[1], A[2] with A[3], etc.). Print the resulting list. If a list has an odd number of elements, leave the last element in place.

#For example, on input:
#1 3 2 6 7
#output must be
#3 1 6 2 7

s = input()

num_strs = s.split()

nums = []
for num_str in num_strs:
  nums.append(int(num_str))
  
for i in range(0, len(nums) -1, 2):
  nums[i], nums[i+1] = nums[i+1], nums[i]

print(nums)
