#First line of the input is a number, which indicates how many pairs of words will follow (each pair in a separate line). The pairs are of the form COUNTRY CITY specifying in which country a city is located. The last line is the name of a city. Print the number of cities that are located in the same country as this city.

#Hint. Use dictionaries. 

#For example, on input:
#6
#UK London
#US Boston
#UK Manchester
#UK Leeds
#US Dallas
#Russia Moscow
#Manchester
#output must be:
#3

city_dict = {}
dict_count = int(input())

while dict_count > 0:
  user_input = input()
  value, key = user_input.split(" ")
  city_dict[key] = value
  dict_count = dict_count - 1

key_input = input()
check_value = city_dict[key_input]
value_count = 0

my_list = list(city_dict.values())

for i in my_list:
  if i == check_value:
    value_count += 1


print(value_count)
