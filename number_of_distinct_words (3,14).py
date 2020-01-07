#Implement a function word_count(s) that, given a string consisting of words separated by spaces, returns how many distinct words it has. 

#For example, the result of 
#print(word_count("Such a day is a bad day"))
#must be
#5

#implement the required function
def word_count(s):
  string = s.split(" ")
  word_list = list(string)
  unique_list = []
  for i in word_list:
    if i not in unique_list:
      unique_list.append(i)
  return(len(unique_list))
