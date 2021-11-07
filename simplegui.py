# imports
import PySimpleGUI as Sg
import shared_vars as v
import virtual_display_controller as outD
import grid_controller as gc

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt
def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def runUI():
    #creating layout
    button_layout = [[Sg.Button('Show Map'), Sg.Button('Pause'), Sg.Button('Close')]]
    mainLayout = [[Sg.B(' ', size=(2, 1), key=(i, j)) for i in range(v.max_x)] for j in range(v.max_y)]
    layout = [
        [Sg.Column(mainLayout, size=(400, 350), key='gridWindow'),Sg.Canvas(key='figCanvas',size=(200, 100))],
        [Sg.Column(button_layout, justification='right')]
    ]
    window = Sg.Window("app", layout)
    frame = 0
    play = False
    grid = gc.create_flat_grid()
    figAgg = False
    # program run loop
    while True:
        event, values = window.read(timeout=100)
        #print (event)
        if event == 'Show Map':
            if figAgg != False:
                figAgg.get_tk_widget().forget()
            fig, ax = outD.showTableState(grid)
            figAgg = draw_figure(window['figCanvas'].TKCanvas, fig)
            play = True
        for i in range(v.max_x):
            for j in range(v.max_y):
                if event == (i, j):
                    print ('pressed: ', i, ', ', j)
                    grid = gc.create_river(grid, i, j)
        if event == 'Pause':
            play = False
        if play:
            frame += 1
            #window['_text_'].update('app is running {}'.format(frame))

        # exit run loop event
        if event == "Close" or event == Sg.WIN_CLOSED:
            break

        window.refresh()

    window.close()
