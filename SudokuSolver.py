board = [
    [0, 0, 0, 0, 0, 0, 0, 0, 8],
    [0, 2, 0, 0, 5, 0, 7, 6, 0],
    [0, 6, 0, 0, 0, 0, 0, 0, 3],
    [5, 0, 0, 0, 0, 0, 2, 0, 7],
    [0, 3, 0, 0, 1, 0, 0, 0, 0],
    [2, 0, 0, 4, 0, 0, 0, 3, 0],
    [0, 0, 0, 6, 0, 0, 0, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 0, 2, 7, 0, 0, 4, 0]
    ]
# function to print out the board
def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("----------------------")

        for j in range(len(bo[i])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            print(str(bo[i][j]) + " ", end = "")
        print()

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
    board[y][x] = 0

# a function to find the first empty space in the board and return its position
def first_empty(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return (i,j)

    return False

def solve(board):
    found = first_empty(board)
    if not found:
        return True
    else:
        pos = first_empty(board)
        for i in range(1, 10):
            if valid_place(pos, i, board):
                # add the pos onto the board
                add_num(i,pos, board)

                if solve(board):
                    return True
                del_num(pos, board)

        return False

solve(board)
print_board(board)