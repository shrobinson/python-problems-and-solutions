#Given two cells of a chessboard. If they are painted in one color, print the word YES, and if in a different color - NO.

#The program receives the input of four numbers from 1 to 8, each specifying the column and row number, first two - for the first cell, and then the last two - for the second cell.

#It is assumed that the cells are numbered from left to right and from bottom to top, i.e., the bottom left cell has column number 1 and row number 1 while the bottom right cell has column number 8 and row number 1.

#For example, on input
#1
#1
#2
#6
#output must be
#YES

col_1 = int(input())
row_1 = int(input())
col_2 = int(input())
row_2 = int(input())

if (col_1 + row_1) % 2 == 0 and (col_2 + row_2) % 2 == 0:
  print("YES")
elif (col_1 + row_1) % 2 != 0 and (col_2 + row_2) % 2 != 0:
  print("YES")
else:
  print("NO")
