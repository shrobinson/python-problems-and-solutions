#You are given a string.
#In the first line, print all but the last two characters of the string.
#In the second line, print all but the first two characters of the string.
#In the third line, print all but the first two characters and the last two characters of the string.

#If the specified segment is empty, print [EMPTY] in the corresponding string.

#For example, on input:
#abracadabra
#output must be
#abracadab
#racadabra
#racadab

word = input()
if word != "" and len(word) > 4:
  print(word[:-2])
  print(word[2:])
  print(word[2:-2])
elif word != "" and len(word) > 2:
  print(word[:-2])
  print(word[2:])
  print("EMPTY")
else:
  print("EMPTY")
  print("EMPTY")
  print("EMPTY")
