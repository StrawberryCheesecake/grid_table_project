# imports
import PySimpleGUI as Sg

# main code
if __name__ == '__main__':
    button_layout = [[Sg.Button('Play'), Sg.Button('Pause'), Sg.Button('Close')]]
    mainLayout = [[Sg.Text('app is waiting to run', key='_text_')]]
    layout = [
        [Sg.Column(mainLayout, size=(400, 400), key='mainWindow')],
        [Sg.Column(button_layout, justification='right')]
    ]
    window = Sg.Window("app", layout)
    frame = 0
    play = False
    # program run loop
    while True:
        event, values = window.read(timeout=100)
        if event == 'Play':
            play = True
        if event == 'Pause':
            play = False
        if play:
            frame += 1
            window['_text_'].update('app is running {}'.format(frame))

        # exit run loop event
        if event == "Close" or event == Sg.WIN_CLOSED:
            break

        window.refresh()

    window.close()
