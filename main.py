#imports
import PySimpleGUI as sg
import time

#main code
if __name__ == '__main__':
    closeBlayout = [[sg.Button('Play'), sg.Button('Pause'), sg.Button('Close')]]
    mainLayout = [[sg.Text('app is waiting to run', key='_text_')]]
    layout = [
        [sg.Column(mainLayout, size=(400, 400), key='mainWindow')],
        [sg.Column(closeBlayout, justification='right')]
    ]
    window = sg.Window("app", layout)
    frame = 0
    play = False
    #program run loop
    while True:
        event, values = window.read(timeout=100)
        if event == 'Play':
            play = True
        if event == 'Pause':
            play = False
        if play:
            frame += 1
            window['_text_'].update('app is running {}'.format(frame))

        #exit run loop event
        if event == "Close" or event == sg.WIN_CLOSED:
            break

        window.refresh()

    window.close()