from SudokuSolver import *
BOARD_LEN = 9

root.title("Sudoku Solver By Anthony Ouch")
root.configure(background = rgbtohex(25,73,114))

def start(board):
    print('hi')
    is_instant[0] = False
    anotherboard = [[0 for row in range(9)] for col in range(9)]
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            val = board[i][j].get()
            anotherboard[i][j] = int(val) if val != '' else val
    solve(anotherboard)

def clear(board):
    clear_clicked[0] = True
    for i in range(BOARD_LEN):
        for j in range(BOARD_LEN):
            sudoku_board[i][j].delete(0,END)

def instant(board):
    is_instant[0] = True


for i in range(9):
    for j in range(9):
        dic = {0: (4,0),  2: (0,4), 5: (0,4), 8: (0,4)}
        currentpady = (0,0)
        currentpadx = (0,0)
        if i in dic:
            currentpady = dic[i]
        if j in dic:
            currentpadx = dic[j]

        tile = Entry(root, width=2, font = ("Arial", 40), highlightbackground = 'black', highlightthickness = 1, justify = 'center')
        tile.grid(row=i, column=j, ipadx=10, ipady=10, padx = currentpadx, pady = currentpady)

        sudoku_board[i][j] = tile

#create button
startbutton = Button(root, width =4, text = "Solve", font= ('Arial', 30), command= lambda: start(sudoku_board))
startbutton.grid(row = 3, column = 9 , padx = 7, ipadx = 20)

instantbutton = Button(root, width=4, text="Instant", font=('Arial',30), command=lambda: instant(sudoku_board))
instantbutton.grid(row=4, column=9,padx=7, ipadx=20)

clearbutton = Button(root, width=4, text = "Clear", font= ('Arial', 30), command= lambda: clear(sudoku_board))
clearbutton.grid(row = 5, column = 9, padx = 7,ipadx =20)

root.mainloop()
