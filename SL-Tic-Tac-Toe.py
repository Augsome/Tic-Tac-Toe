# Need to repeat to have 9 total prompts to fill the board

# the following code creates the board
board = [["-", "-", "-"],
         ["-", "-", "-"],
         ["-", "-", "-"]]

print(board[0])
print(board[1])
print(board[2])

#this is player X's first move
column = int(input("X player, select a column 1-3: "))
row = int(input("X player, select a row 1-3: "))
column -= 1
row -= 1

board[row][column] = "X"
print(board[0])
print(board[1])
print(board[2])

#this is player O's first move
column = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
column -= 1
row -= 1

if board[row][column] == "-":
    board[row][column] == "O"
else:
    print("Oops, that spot was already taken.")
    
board[row][column] = "O"
print(board[0])
print(board[1])
print(board[2])

#this is player X's second move
column = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
column -= 1
row -= 1

if board[row][column] == "-":
    board[row][column] == "X"
else:
    print("Oops, that spot was already taken.")
    
board[row][column] = "X"
print(board[0])
print(board[1])
print(board[2])

#this is player O's second move
column = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
column -= 1
row -= 1

if board[row][column] == "-":
    board[row][column] == "O"
else:
    print("Oops, that spot was already taken.")
    
board[row][column] = "O"
print(board[0])
print(board[1])
print(board[2])

#this is player X's third move
column = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
column -= 1
row -= 1

if board[row][column] == "-":
    board[row][column] == "X"
else:
    print("Oops, that spot was already taken.")
    
board[row][column] = "X"
print(board[0])
print(board[1])
print(board[2])

#this is player O's third move
column = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
column -= 1
row -= 1

if board[row][column] == "-":
    board[row][column] == "O"
else:
    print("Oops, that spot was already taken.")
    
board[row][column] = "O"
print(board[0])
print(board[1])
print(board[2])

#this is player X's fourth move
column = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
column -= 1
row -= 1

if board[row][column] == "-":
    board[row][column] == "X"
else:
    print("Oops, that spot was already taken.")
    
board[row][column] = "X"
print(board[0])
print(board[1])
print(board[2])

#this is player O's fourth move
column = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
column -= 1
row -= 1

if board[row][column] == "-":
    board[row][column] == "O"
else:
    print("Oops, that spot was already taken.")
    
board[row][column] = "O"
print(board[0])
print(board[1])
print(board[2])

#this is player X's fifth move
column = int(input("O player, select a column 1-3: "))
row = int(input("O player, select a row 1-3: "))
column -= 1
row -= 1

if board[row][column] == "-":
    board[row][column] == "X"
else:
    print("Oops, that spot was already taken.")
    
board[row][column] = "X"
print(board[0])
print(board[1])
print(board[2])