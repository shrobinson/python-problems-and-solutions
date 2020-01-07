#Chess rook moves horizontally or vertically on the chessboard. Given two different cells of the chessboard, determine whether a rook can go from the first cell to the second in one move.

#The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a rook can go from the first cell to the second in one move, or NO otherwise.

#For example, on input
#2
#3
#5
#6
#output must be 
#NO

col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if col_1 == col_2 or row_1 == row_2:
  print("YES")
else:
  print("NO")
