from tkinter import *
import random
from tkinter import ttk
from PIL import ImageTk, Image
PuzzleWindow = Tk()


# img = ImageTk.PhotoImage(Image.open("bild.gif"))
# panel = Label(PuzzleWindow, image=img)
# panel.place(side="bottom", fill="both", expand="yes")
# PuzzleWindow.mainloop()

PuzzleWindow.title('Memory Puzzle')
tabs = ttk.Notebook(PuzzleWindow)
easy = ttk.Frame(tabs)
tabs.add(easy, text='Easy')
tabs.pack(expand=1, fill="both")

"""Level 1"""


def draw(a, x, y):
    """ x = row index, y = column index"""
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
    global base1, ans1, board1, moves1
    count = 0
    for i in range(4):
        for j in range(4):
            base1.create_rectangle(100 * i, j * 100, 100 * i + 100, 100 * j + 100, fill="white")
            if board1[i][j] != '.':
                draw(board1[i][j], i, j)
                count += 1
    if count == 16:
        base1.create_text(200, 450, text="No. of moves: " + str(moves1), font=('arial', 30))


def call(event):
    global base1, ans1, board1, moves1, prev1
    i = event.x // 100
    j = event.y // 100
    if board1[i][j] != '.':
        return
    moves1 += 1
    # print(moves)
    if prev1[0] > 4:
        prev1[0] = i
        prev1[1] = j
        board1[i][j] = ans1[i][j]
        quizboard()
    else:
        board1[i][j] = ans1[i][j]
        quizboard()
        if ans1[i][j] == board1[prev1[0]][prev1[1]]:
            print("matched")
            prev1 = [100, 100]
            quizboard()
            return
        else:
            board1[prev1[0]][prev1[1]] = '.'
            quizboard()
            prev1 = [i, j]
            return


base1 = Canvas(easy, width=500, height=500)
base1.pack()

ans1 = list('AABBCCDDEEFFGGHH')
random.shuffle(ans1)
ans1 = [ans1[:4],
        ans1[4:8],
        ans1[8:12],
        ans1[12:]]

base1.bind("<Button-1>", call)

moves1 = 0

prev1 = [100, 100]

board1 = [list('.' * 4) for count in range(4)]
quizboard()
mainloop()
