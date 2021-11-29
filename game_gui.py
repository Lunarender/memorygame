import memory_game2
import PySimpleGUI as sg


def make_win1():
    sg.theme('DarkBlue12')
    layout = [[sg.Text('Welcome to Memory Game', font='Arial 20 bold')],
              [sg.Text('Click exit to exit the game')],
              [sg.Text('')],
              [sg.Text('')],
              [sg.Text('')],
              [sg.Text('')],
              [sg.Text('')],
              [sg.Button('Play', font='Arial 20 bold')],
              [sg.Button('Game_rules', font='Arial 20 bold')],
              [sg.Button('Exit', font='Arial 20 bold')]]

    return sg.Window('Memory Game', layout, element_justification='c', size=(1000, 600), finalize=True)


window1, window2 = make_win1(), None        # start off with 1 window open
while True:             # Event Loop
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == window2:       # if closing win 2, mark as closed
            window2 = None
        elif window == window1:     # if closing win 1, exit program
            break
    elif event == 'Game_rules':
        sg.popup('Match same objects', 'User will get 10 points for each matching', 'After matching all '
                 'objects of the window, user will reach the next level', font='Arial 16 bold')
    elif event == 'Play' and not window2:
        window2 = memory_game2.main()
    elif event == '-IN-':
        window['-OUTPUT-'].update(f'You enetered {values["-IN-"]}')
    elif event == 'Erase':
        window['-OUTPUT-'].update('')
        window['-IN-'].update('')
window.close()
