#In chess, the bishop moves diagonally, any number of squares. Given two different squares of the chessboard, determine whether a bishop can go from the first to the second in one move.

#The program receives as input four numbers from 1 to 8, specifying the column and row numbers of the starting square and the column and row numbers of the ending square. The program should output YES if a Bishop can go from the first square to the second in one move, or NO otherwise.

#For example, on input
#2
#3
#5
#6
#output must be
#YES

col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if abs(col_1 - col_2) == abs(row_1 - row_2):
  print("YES")
else:
  print("NO")
