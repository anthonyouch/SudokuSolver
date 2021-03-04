# function to print out the board

from time import *
from tkinter import *
from tkinter import messagebox

sudoku_board = [[0 for row in range(9)] for col in range(9)]
root = Tk()
clear_clicked = [False]
is_instant = [False]

def rgbtohex(r,g,b):
    return f'#{r:01x}{g:02x}{b:02x}'

#given a pos and num check to see if it's valid to add the num at that position
def valid_place(pos, num, board):
    # everything in that row can not be equal to num
    y, x = pos
    for i in board[y]:
        if i == num:
            return False
    #everything in that column must not equal to num
    for row in board:
        if row[x] == num:
            return False
    #everything in the box must not equal to num

    for i in range(y//3 * 3, y//3 * 3 + 3):
        for j in range(x//3 * 3, x//3 * 3 + 3):

            if board[i][j] == num:
                return False
    return True

# a function to add the number into the position
def add_num(num, pos, board):
    y,x = pos
    board[y][x] = num

# a function to delete the number from the board
def del_num(pos, board):
    y,x = pos
    board[y][x] = ''

# a function to find the first empty space in the board and return its position
def first_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == '':
                return (i,j)

    return False

def solve(board):
    global clear_clicked

    found = first_empty(board)
    if not found:
        return True
    else:
        pos = first_empty(board)
        for i in range(1, 10):

            if clear_clicked[0] == True:
                clear_clicked[0] = False
                return True

            sudoku_board[pos[0]][pos[1]].delete(0, END)
            sudoku_board[pos[0]][pos[1]].insert(0, i)

            if is_instant[0] == False:
                root.update()
                sleep(0.01)

            if valid_place(pos, i, board):
                # add the pos onto the board

                add_num(i, pos, board)

                if solve(board):
                    return True
                else:
                    del_num(pos, board)

        sudoku_board[pos[0]][pos[1]].delete(0, END)
        return False



