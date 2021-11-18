from tkinter import *
import random
from tkinter import ttk
from pygame import *
import pygame

PuzzleWindow = Tk()
PuzzleWindow.title(' Minnes Spel ')
tabs = ttk.Notebook(PuzzleWindow)
easy = ttk.Frame(tabs)

tabs.add(easy, text='Enkel')
tabs.pack(expand=10, fill="both")


def add_background_music():
    """Adding background music"""
    pygame.mixer.init()
    pygame.mixer.music.load('crash.wav.mp3')
    pygame.mixer.music.play(loops=-1)


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
            base1.create_rectangle(100 * i, j * 100, 100 * i + 100, 100 * j + 100, fill="cyan")
            if board1[i][j] != '.':
                draw(board1[i][j], i, j)
                count += 1
    if count == 16:
        base1.create_text(200, 450, text="Antal drag: " + str(moves1), font=('arial', 30))


def call(event):
    """This function gets executed every time the user clicks a card.
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


base1 = Canvas(easy, width=500, height=500)
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
board1 = [list('.' * 4) for count in range(4)]
quizboard()
add_background_music()
mainloop()
