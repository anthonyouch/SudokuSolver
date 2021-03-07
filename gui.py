from SudokuSolver import *
BOARD_LEN = 9

root.title("Sudoku Solver By Anthony Ouch")
root.configure(background = rgbtohex(25,73,114))

red_count = 0

def start():

    global stop_validation
    global board2
    solve_started[0] = True
    stop_validation[0] = True
    instantbutton['state'] = "active"
    startbutton['state'] = "disabled"

    is_instant[0] = False
    clear_clicked[0] = False
    solve(board2)

def clear():
    global stop_validation
    global sudoku_board
    global board2
    global cnt
    global check_fail

    cnt[0] = 0
    check_fail = list()

    solve_started[0] = False
    stop_validation[0] = False
    board2 = [['' for row in range(BOARD_LEN)] for col in range(BOARD_LEN)]
    startbutton['state'] = "active"
    instantbutton['state'] = "disabled"

    clear_clicked[0] = True
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            sudoku_board[i][j].delete(0,END)
    
def instant():
    global is_instant

    instantbutton['state'] = "disabled"
    is_instant[0] = True


def check_if_alone(pos, board2, s):
    count = 0
    for i in range(len(board2[pos[0]])):
        if board2[pos[0]][i] == s:
            count += 1

    for row in range(len(board2)):
        if board2[row][pos[1]] == s:
            count += 1

    for i in range(pos[0] // 3 * 3, pos[0] // 3 * 3 + 3):
        for j in range(pos[1] // 3 * 3, pos[1] // 3 * 3 + 3):
            if board2[i][j] == s:
                count += 1

    return count - 2

def redboxes_ammount():
    global sudoku_board
    count = 0
    for row in sudoku_board:
        for box in row:
            if box['bg'] == "red":
                count += 1
    return count

def validate(P, s, i, j):
    #P has to be either 1-10 or empty
    global board2
    global stop_validation
    global red_count

    s = int(s) if s != '' else ''

    pos = (int(i),int(j))
    global sudoku_board
    if P == '':
        if not stop_validation[0]:
            sudoku_board[pos[0]][pos[1]]['bg'] = 'white'
            board2[pos[0]][pos[1]] = ''

            #check removal
            for i in range(len(board2[pos[0]])):
                if board2[pos[0]][i] == s:
                    count = check_if_alone((pos[0], i), board2, s)
                    if count == 1:
                        sudoku_board[pos[0]][i]['bg'] = 'light green'
                        red_count -= 1

            for row in range(len(board2)):
                if board2[row][pos[1]] == s:
                    count = check_if_alone((row, pos[1]), board2, s)
                    if count == 1:
                        sudoku_board[row][pos[1]]['bg'] = 'light green'
                        red_count -= 1

            for i in range(pos[0] // 3 * 3, pos[0] // 3 * 3 + 3):
                for j in range(pos[1] // 3 * 3, pos[1] // 3 * 3 + 3):
                    if board2[i][j] == s:
                        count = check_if_alone((i, j), board2, s)
                        if count == 1:
                            sudoku_board[i][j]['bg'] = 'light green'
                            red_count -= 1

            if redboxes_ammount() == 0:
                startbutton['state'] = 'active'

    #if there is only 1 other red one of the same number
        return True
    if P in [str(i) for i in range(10)]:
        if not stop_validation[0]:
            #check to see if they add it in a proper position if not, turn the box red
            invalid_poses = valid_place(pos, int(P), board2)

            if len(invalid_poses) > 0:
                for invalid_pos in invalid_poses:
                    sudoku_board[invalid_pos[0]][invalid_pos[1]]['bg'] = 'red'
                    sudoku_board[pos[0]][pos[1]]['bg'] = 'red'
            else:
                sudoku_board[pos[0]][pos[1]]['bg'] = 'light green'

            board2[int(i)][int(j)] = int(P) if P != '' else ''

            if redboxes_ammount() > 0:
                startbutton['state'] = 'disabled'

        return True

    return False

for i in range(9):
    for j in range(9):
        vcmd = root.register(validate)
        dic = {0: (4,0),  2: (0,4), 5: (0,4), 8: (0,4)}
        currentpady = (0,0)
        currentpadx = (0,0)
        if i in dic:
            currentpady = dic[i]
        if j in dic:
            currentpadx = dic[j]

        tile = Entry(root, width=2, font = ("Arial", 40), highlightbackground = "black", highlightthickness = 1,
                    justify="center", validate="key", validatecommand=(vcmd, '%P', '%s', i, j))
        tile.grid(row=i, column=j, ipadx=10, ipady=10, padx = currentpadx, pady = currentpady)

        sudoku_board[i][j] = tile

#create button
startbutton = Button(root, width =4, text = "Solve", font= ('Arial', 30), command=start)
startbutton.grid(row = 3, column = 9 , padx = 7, ipadx = 20)

instantbutton = Button(root, width=4, text="Instant", font=('Arial',30), command=instant,
                       state="disabled")
instantbutton.grid(row=4, column=9,padx=7, ipadx=20)

clearbutton = Button(root, width=4, text = "Clear", font= ('Arial', 30), command=clear)
clearbutton.grid(row = 5, column = 9, padx = 7,ipadx =20)

root.mainloop()
#to do list
# if its invalid board, go red
# if it's unsolvable pop window unsolvable
# can only enter num 1-9
# after clicking solve, make it unclickable
# cannot click instant before solve
# maybe cannot click clear when its empty
# create icon for program
