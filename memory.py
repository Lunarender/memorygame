import random
import tkinter

def draw(a, l, m):
    global base1
    if a == 'A':
        d = base1.create_rectangle(100 * l + 20, m * 100 + 20, 100 * l + 100 - 20, 100 * m + 100 - 20, fill='red')
    elif a == 'B':
        d = base1.create_rectangle(100 * l + 20, m * 100 + 20, 100 * l + 100 - 20, 100 * m + 100 - 20, fill='yellow')
    elif a == 'C':
        d = base1.create_rectangle(100 * l + 20, m * 100 + 20, 100 * l + 100 - 20, 100 * m + 100 - 20, fill='blue')
    elif a == 'D':
        d = base1.create_oval(100 * l + 20, m * 100 + 20, 100 * l + 100 - 20, 100 * m + 100 - 20, fill='red')
    elif a == 'E':
        d = base1.create_oval(100 * l + 20, m * 100 + 20, 100 * l + 100 - 20, 100 * m + 100 - 20, fill='yellow')
    elif a == 'F':
        d = base1.create_oval(100 * l + 20, m * 100 + 20, 100 * l + 100 - 20, 100 * m + 100 - 20, fill='blue')
    elif a == 'G':
        d = base1.create_polygon(100 * l + 50, m * 100 + 20, 100 * l + 20, 100 * m + 100 - 20, 100 * l + 100 - 20,
                                 100 * m + 100 - 20, fill='red')
    elif a == 'H':
        d = base1.create_polygon(100 * l + 50, m * 100 + 20, 100 * l + 20, 100 * m + 100 - 20, 100 * l + 100 - 20,
                                 100 * m + 100 - 20, fill='green')


def quizboard():
    global base1, ans1, board1, moves1
    count = 0
    for i in range(4):
        for j in range(4):
            rec = base1.create_rectangle(100 * i, j * 100, 100 * i + 100, 100 * j + 100, fill="white")
            if (board1[i][j] != '.'):
                draw(board1[i][j], i, j)
                count += 1
    if count == 16:
        base1.create_text(200, 450, text="No. of moves: " + str(moves1), font=('arial', 20))


def call(event):
    global base1, ans1, board1, moves1, prev1
    i = event.x // 100
    j = event.y // 100
    if board1[i][j] != '.':
        return
    moves1 += 1
    # print(moves)
    if (prev1[0] > 4):
        prev1[0] = i
        prev1[1] = j
        board1[i][j] = ans1[i][j]
        quizboard()
    else:
        board1[i][j] = ans1[i][j]
        quizboard()
        if (ans1[i][j] == board1[prev1[0]][prev1[1]]):
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

moves1 = IntVar()
moves1 = 0

prev1 = [100, 100]

board1 = [list('.' * 4) for count in range(4)]
quizboard()