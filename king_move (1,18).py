#Chess king moves horizontally, vertically or diagonally to any adjacent cell. Given two different cells of the chessboard, determine whether a king can go from the first cell to the second in one move.

#The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell. The program should output YES if a king can go from the first cell to the second in one move, or NO otherwise.

#For example, on input
#2
#3
#1
#4
#output should be 
#YES

col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if abs(col_1 - col_2) <=1 and abs(row_1 - row_2) <= 1 :
  print("YES")
else:
  print("NO")
