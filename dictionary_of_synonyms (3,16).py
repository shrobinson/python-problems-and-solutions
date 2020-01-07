#You are given a dictionary consisting of word pairs. Every word is a synonym the other word in its pair. All the words in the dictionary are different.

#First line of the input specifies how many word pairs will follow. After the dictionary there is one more word given. Find a synonym for this word.

#Hint. To solve the problem quickly, use dictionaries.

#For example, on input
#3
#water liquid
#fire heat
#python java
#fire
#output must be
#heat

synonym_dict = {}
dict_count = int(input())

while dict_count > 0:
  user_input = input()
  key, value = user_input.split(" ")
  synonym_dict[key] = value
  dict_count = dict_count - 1

key_input = input()

print(synonym_dict[key_input])
