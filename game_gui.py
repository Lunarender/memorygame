import mg_version1
import mg_version2
import PySimpleGUI as sg


def make_win1():
    sg.theme('DarkBlue12')
    layout = [[sg.Text('')],
              [sg.Text('Welcome to Memory Game', font='Algerian 30 bold italic')],
              [sg.Text('Click exit to exit the game')],
              [sg.Text('')],
              [sg.Text('')],
              [sg.Text('')],
              [sg.Button('Play_version1', font='Arial 20 bold', button_color=('black', 'white'))],
              [sg.Button('Play_version2', font='Arial 20 bold', button_color=('black', 'white'))],
              [sg.Button('Game_rules', font='Arial 18 bold', button_color=('black', 'white'))],
              [sg.Button('Exit', font='Arial 18 bold', button_color=('black', 'white'))]]

    return sg.Window('Memory Game', layout, element_justification='c', size=(1000, 600), finalize=True)


def main():
    window1, window2 = make_win1(), None  # start off with 1 window open

    while True:             # Event Loop
        window, event, values = sg.read_all_windows()
        if event == sg.WIN_CLOSED or event == 'Exit':
            window.close()
            if window == window2:       # if closing win 2, mark as closed
                window2 = None
            elif window == window1:     # if closing win 1, exit program
                break
        elif event == 'Game_rules':
            sg.popup('Match same objects', 'User will get 10 points for each matching(version1)', 'After matching all '
                     'objects of the window, user will reach the next level', font='Arial 14 bold')
        elif event == 'Play_version1':
            mg_version1.main()
        elif event == 'Play_version2':
            mg_version2.main()
    window.close()


if __name__ == '__main__':
    main()
