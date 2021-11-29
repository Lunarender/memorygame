import memory_game2
import memory_game
import PySimpleGUI as sg


def make_win1():
    sg.theme('DarkBlue12')
    layout = [[sg.Text('Welcome to Memory Game', font='Arial 30 bold italic')],
              [sg.Text('')],
              [sg.Text('Click exit to exit the game')],
              [sg.Text('')],
              [sg.Text('')],
              [sg.Text('')],
              [sg.Button('Play_version1', font='Arial 20 bold', button_color=('black', 'white'))],
              [sg.Button('Play_version2', font='Arial 20 bold', button_color=('black', 'white'))],
              [sg.Button('Game_rules', font='Arial 20 bold', button_color=('black', 'white'))],
              [sg.Button('Exit', font='Arial 20 bold', button_color=('black', 'white'))]]

    return sg.Window('Memory Game', layout, element_justification='c', size=(1000, 600), finalize=True)


window1 = make_win1()
window2, window3 = None, None        # start off with 1 window open
while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
        if window == window3:       # if closing win 3, mark as closed
            window3 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Game_rules':
        sg.popup('Match same objects', 'User will get 10 points for each matching', 'After matching all '
                 'objects of the window, user will reach the next level', font='Arial 16 bold')
    elif event == 'Play_version1':
        window2 = memory_game2.main()
    elif event == 'Play_version2':
        window3 = memory_game.mainloop()
window.close()
