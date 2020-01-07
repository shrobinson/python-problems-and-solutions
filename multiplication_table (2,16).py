#Give two numbers N and M, print the multiplication table with N rows and M columns. In the cell at the row i and column j print the value of i*j. The cells must be separated by space horizontally.

#Hint. Use nested loops.

#For example, on input
#5
#3
#output must be
#1 2 3
#2 4 6
#3 6 9
#4 8 12
#5 10 15

n = int(input())
m = int(input())
for i in range(1, n+1):
  for j in range(1, m+1):
    mult = i*j
    print (mult, end = " ")
  print()
