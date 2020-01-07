#There was a set of cards with numbers from 1 to N. One of the card is now lost. Determine the number on that lost card given the numbers for the remaining cards.
#Given a number N, followed by N − 1 integers - representing the numbers on the remaining cards (distinct integers in the range from 1 to N). Find and print the number on the lost card.

#Recommendation. Use for loops.

#For example, on input
#4
#3
#1
#4
#output must be
#2

N = int(input())
total = 0
real_total = 0
for i in range (1, N):
  value = int(input())
  real_total += value
for i in range (1, N+1):
  total += i
print(total-real_total)
    
