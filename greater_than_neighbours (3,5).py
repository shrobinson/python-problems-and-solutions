#Given a list of numbers, determine and print the quantity of elements that are greater than both of their neighbors.

#The first and the last items of the list shouldn't be considered because they don't have two neighbors.

#For example, on input
#1 2 3 2 8 7 6 9 5
#output must be
#3

s = input()

num_strs = s.split()

nums = []
for num_str in num_strs:
  nums.append(int(num_str))

count = 0

for i in range(1, len(nums)-1):
  if nums[i+1] < nums[i] and nums[i] > nums[i-1]:
    count += 1
print(count)
