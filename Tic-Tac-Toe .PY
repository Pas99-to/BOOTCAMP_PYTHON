
from random import randrange

def display_board(board):
    print("+--------+ "*3)
    for row in range(len(board)):
        print("|        | "*3)
        for colum in range(len(board)):
            print("|    " + str(board[row][colum]) + "   |",end=" ")
        print("   ")
        print("|        | "*3)
        print("+--------+ "*3)

def enter_move(board):
    # The function accepts the board's current status, asks the user about their move, 
    # checks the input, and updates the board according to the user's decision.
    len_array = len(board)
    enter_move = str(input("Enter your move: "))
    if int(enter_move) >= 0 and int(enter_move) <= 9:
        for move_row in range(len_array):
            for move_colum in range(len_array):
                if enter_move == str(board[move_row][move_colum]):
                    board[move_row][move_colum] = "O"
                    break

def make_list_of_free_fields(board):
    # The function browses the board and builds a list of all the free squares; 
    # the list consists of tuples, while each tuple is a pair of row and column numbers.
    free_squares =  []
    for row in range(3):
        for colum in range(3):
            if board[row][colum] not in ["O","X"]:
                free_squares.append((row,colum))
    return free_squares

def victory_for(board, sign):
    # The function analyzes the board's status in order to check if 
    # the player using 'O's or 'X's has won the game
    if sign == "O":
        who = "You"
    elif sign == "X":
        who = "Me"
    else:
        who = None
    diagonal_1 = diagonal_2 = True
    for i in range(3):
        
        if board[i][0] == sign and board[i][1] == sign and board[i][2] == sign:
            return who
        if board[0][i] == sign and board[1][i] == sign and board[2][i] == sign:
            return who
        if board[i][i] != sign:
            diagonal_1 = False
        if board[2 - i][i] != sign:
            diagonal_2 = False
    if diagonal_1 or diagonal_2:
        return who
    return None

def draw_move(board):
    # The function draws the computer's move and updates the board.
    free = make_list_of_free_fields(board)
    rando = randrange(0,len(free)+1)
    row, col = free[rando]
    board[row][col] = "X"


board = [[3*j+i+1 for i in range(3)] for j in range(3)]
board[1][1]="X"
libre = make_list_of_free_fields(board)
turno = True

while len(libre):
    display_board(board)
    if turno:
        enter_move(board)
        victoria = victory_for(board,"O")
    else:
        draw_move(board)
        victoria = victory_for(board,"X")
    if victoria != None:
        break
    turno = not turno
    libre  = make_list_of_free_fields(board)

display_board(board)
if victoria == "You":
    print("Ganaste :)")
elif victoria == "Me":
    print("Gane Yo :), Suerte para la PROXIMA :(")
else:
    print("Quedamos empate")