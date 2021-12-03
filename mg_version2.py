from tkinter import *
import random
from tkinter import ttk

global PuzzleWindow, tabs, easy, base1, base2, base3, ans1, ans2, ans3, board3, moves3, prev3, board2, moves2,\
        prev2, board1, moves1, prev1, window2, window3

""" ttk.Notebook() manages the collection of windows and displays one window at a time.
ttk.Frame() is basically a rectangular container for other widgets."""

"""Level 1"""


def draw(a, x, y):
    """This function displays the card present at row index x and
     column index y by creating a shape of assigned color."""
    global base1
    if a == 'A':
        base1.create_rectangle(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='red')
    elif a == 'B':
        base1.create_rectangle(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='yellow')
    elif a == 'C':
        base1.create_rectangle(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='blue')
    elif a == 'D':
        base1.create_oval(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='red')
    elif a == 'E':
        base1.create_oval(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='yellow')
    elif a == 'F':
        base1.create_oval(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='blue')
    elif a == 'G':
        base1.create_polygon(100 * x + 50, y * 100 + 20, 100 * x + 20, 100 * y + 100 - 20, 100 * x + 100 - 20,
                             100 * y + 100 - 20, fill='red')
    elif a == 'H':
        base1.create_polygon(100 * x + 50, y * 100 + 20, 100 * x + 20, 100 * y + 100 - 20, 100 * x + 100 - 20,
                             100 * y + 100 - 20, fill='green')


def quizboard():
    """It runs two for loops and creates a 100×100 rectangle for each cell of the 4×4 grid."""
    global base1, ans1, board1, moves1
    count = 0
    for i in range(4):
        for j in range(4):
            base1.create_rectangle(100 * i, j * 100, 100 * i + 100, 100 * j + 100, fill="royalBlue")
            if board1[i][j] != '.':
                draw(board1[i][j], i, j)
                count += 1
    if count == 16:
        base1.create_text(200, 450, text="No. of moves: " + str(moves1), font=('arial', 30))


def call(event):
    """This function gets executed every time the user clicks a card.
    It displays the figures hidden in the tile.
    prev1: a list that stores the row and column index of previously clicked cell."""

    global base1, ans1, board1, moves1, prev1
    i = event.x // 100
    j = event.y // 100
    if board1[i][j] != '.':
        return
    moves1 += 1
    if prev1[0] > 4:
        prev1[0] = i
        prev1[1] = j
        board1[i][j] = ans1[i][j]
        quizboard()
    else:
        board1[i][j] = ans1[i][j]
        quizboard()
        if ans1[i][j] == board1[prev1[0]][prev1[1]]:
            print("Matchade")
            prev1 = [100, 100]
            quizboard()
            return
        else:
            board1[prev1[0]][prev1[1]] = '.'
            quizboard()
            prev1 = [i, j]
            return

"""Level 2"""


def draw1(a, x, y):
    global base2
    if a == 'A':
        base2.create_rectangle(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='red')
    elif a == 'B':
        base2.create_rectangle(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='yellow')
    elif a == 'C':
        base2.create_rectangle(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='blue')
    elif a == 'D':
        base2.create_oval(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='red')
    elif a == 'E':
        base2.create_oval(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='yellow')
    elif a == 'F':
        base2.create_oval(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='blue')
    elif a == 'G':
        base2.create_polygon(100 * x + 50, y * 100 + 20, 100 * x + 20, 100 * y + 100 - 20, 100 * x + 100 - 20,
                             100 * y + 100 - 20, fill='red')
    elif a == 'H':
        base2.create_polygon(100 * x + 50, y * 100 + 20, 100 * x + 20, 100 * y + 100 - 20, 100 * x + 100 - 20,
                             100 * y + 100 - 20, fill='green')
    elif a == 'I':
        base2.create_polygon(100 * x + 50, y * 100 + 20, 100 * x + 20, 100 * y + 100 - 20, 100 * x + 100 - 20,
                             100 * y + 100 - 20, fill='yellow')
    elif a == 'J':
        base2.create_polygon(100 * x + 50, y * 100 + 20, 100 * x + 20, 100 * y + 100 - 20, 100 * x + 100 - 20,
                             100 * y + 100 - 20, fill='blue')
    elif a == 'K':
        base2.create_polygon(100 * x + 50, y * 100 + 20, 100 * x + 20, 100 * y + 100 - 20, 100 * x + 100 - 20,
                             100 * y + 100 - 20, fill='black')
    elif a == 'L':
        base2.create_polygon(100 * x + 50, y * 100 + 20, 100 * x + 20, 100 * y + 100 - 20, 100 * x + 100 - 20,
                             100 * y + 100 - 20, fill='orange')
    elif a == 'M':
        base2.create_rectangle(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='black')
    elif a == 'N':
        base2.create_rectangle(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='orange')
    elif a == 'O':
        base2.create_rectangle(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='green')
    elif a == 'P':
        base2.create_oval(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='black')
    elif a == 'Q':
        base2.create_oval(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='orange')
    elif a == 'R':
        base2.create_oval(100 * x + 20, y * 100 + 20, 100 * x + 100 - 20, 100 * y + 100 - 20, fill='green')


def puzzleboard2():
    global base2, ans2, board2, moves2
    count = 0
    for i in range(6):
        for j in range(6):
            base2.create_rectangle(100 * i, j * 100, 100 * i + 100, 100 * j + 100, fill="royalBlue")
            if board2[i][j] != '.':
                draw1(board2[i][j], i, j)
                count += 1
    if count >= 36:
        base2.create_text(300, 650, text="No. of moves: " + str(moves2), font=('arial', 20))


def call2(event):
    global base2, ans2, board2, moves2, prev2
    i = event.x // 100
    j = event.y // 100
    if board2[i][j] != '.':
        return
    moves2 += 1
    if prev2[0] > 6:
        prev2[0] = i
        prev2[1] = j
        board2[i][j] = ans2[i][j]
        puzzleboard2()
    else:
        board2[i][j] = ans2[i][j]
        puzzleboard2()
        if ans2[i][j] == board2[prev2[0]][prev2[1]]:
            prev2 = [100, 100]
            puzzleboard2()
            return
        else:
            board2[prev2[0]][prev2[1]] = '.'
            puzzleboard2()
            prev2 = [i, j]
            return


def draw2(a, x, y):
    global base3
    if a == 'A':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='red')
    elif a == 'B':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='yellow')
    elif a == 'C':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='blue')
    elif a == 'D':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='red')
    elif a == 'E':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='yellow')
    elif a == 'F':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='blue')
    elif a == 'G':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='red')
    elif a == 'H':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='green')
    elif a == 'I':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='yellow')
    elif a == 'J':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='blue')
    elif a == 'K':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='black')
    elif a == 'L':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='orange')
    elif a == 'M':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='black')
    elif a == 'N':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='orange')
    elif a == 'O':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='green')
    elif a == 'P':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='pink')
    elif a == 'Q':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='green')
    elif a == 'R':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='pink')
    elif a == 'S':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='purple')
    elif a == 'T':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='purple')
    elif a == 'U':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='purple')
    elif a == 'V':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='pink')
    elif a == 'W':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='maroon')
    elif a == 'X':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='maroon')
    elif a == 'Y':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='maroon')
    elif a == 'Z':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='brown')
    elif a == 'a':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='brown')
    elif a == 'b':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='brown')
    elif a == 'c':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='aqua')
    elif a == 'd':
        base3.create_rectangle(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='aqua')
    elif a == 'e':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='aqua')
    elif a == 'f':
        base3.create_polygon(80 * x + 50, y * 80 + 20, 80 * x + 20, 80 * y + 80 - 20, 80 * x + 80 - 20,
                             80 * y + 80 - 20, fill='magenta')
    elif a == 'g':
        base3.create_oval(80 * x + 20, y * 80 + 20, 80 * x + 80 - 20, 80 * y + 80 - 20, fill='magenta')


def quizboard3():
    global base3, ans3, board3, moves3
    count = 0
    for i in range(8):
        for j in range(8):
            base3.create_rectangle(80 * i, j * 80, 80 * i + 80, 80 * j + 80, fill="royalBlue")
            if board3[i][j] != '.':
                draw2(board3[i][j], i, j)
                count += 1
    if count >= 64:
        base3.create_text(300, 650, text="No. of moves: " + str(moves3), font=('arial', 20))


def call3(event):
    global base3, ans3, board3, moves3, prev3
    i = event.x // 80
    j = event.y // 80
    if board3[i][j] != '.':
        return
    moves3 += 1
    if prev3[0] > 8:
        prev3[0] = i
        prev3[1] = j
        board3[i][j] = ans3[i][j]
        quizboard3()
    else:
        board3[i][j] = ans3[i][j]
        quizboard3()
        if ans3[i][j] == board3[prev3[0]][prev3[1]]:
            print("matched")
            prev3 = [100, 100]
            quizboard3()
            return
        else:
            board3[prev3[0]][prev3[1]] = '.'
            quizboard3()
            prev3 = [i, j]
            return


def main():
    global PuzzleWindow, tabs, easy, base1, base2, base3, ans1, ans2, ans3, board3, moves3, prev3, board2, moves2,\
        prev2, board1, moves1, prev1, window2, window3

    PuzzleWindow = Tk()
    PuzzleWindow.title(' Memory Game ')
    tabs = ttk.Notebook(PuzzleWindow)
    easy = ttk.Frame(tabs)
    """ Level 1"""
    base1 = Canvas(easy, width=400, height=500)
    base1.pack()

    ans1 = list('AABBCCDDEEFFGGHH')
    """Simple capital letters are used to denote the pairs and later
     in the draw function, a shape and color have associated for each letter. 
     So, ans1 is basically a well-shuffled 4×4 matrix of letters."""
    random.shuffle(ans1)
    ans1 = [ans1[:4],
            ans1[4:8],
            ans1[8:12],
            ans1[12:]]

    base1.bind("<Button-1>", call)
    moves1 = 0
    prev1 = [100, 100]
    board1 = [list('.' * 4) for _ in range(4)]
    quizboard()

    """level 2"""
    window2 = ttk.Frame(tabs)
    base2 = Canvas(window2, width=700, height=700)
    base2.pack()
    ans2 = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRR')
    random.shuffle(ans2)
    ans2 = [ans2[:6],
            ans2[6:12],
            ans2[12:18],
            ans2[18:24],
            ans2[24:30],
            ans2[30:]
            ]
    base2.bind("<Button-1>", call2)

    moves2 = 0
    prev2 = [100, 100]
    board2 = [list('.' * 6) for _ in range(6)]
    puzzleboard2()

    """level 3"""
    window3 = ttk.Frame(tabs)
    tabs.add(easy, text='Easy')
    tabs.add(window2, text='Medium')
    tabs.add(window3, text='Hard')
    tabs.pack(expand=10, fill="both")

    base3 = Canvas(window3, width=700, height=700)
    base3.pack()

    ans3 = list('AABBCCDDEEFFGGHHIIJJKKLLMMNNOOPPQQRRSSTTUUWWXXYYZZaabbccddeeffgg')
    random.shuffle(ans3)
    ans3 = [ans3[:8],
            ans3[8:16],
            ans3[16:24],
            ans3[24:32],
            ans3[32:40],
            ans3[40:48],
            ans3[48:56],
            ans3[56:]
            ]

    base3.bind("<Button-1>", call3)

    moves3 = 0

    prev3 = [80, 80]

    board3 = [list('.' * 8) for _ in range(8)]
    quizboard3()
    mainloop()


if __name__ == '__main__':
    main()
