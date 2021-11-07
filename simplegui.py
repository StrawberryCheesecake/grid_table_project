# imports
import PySimpleGUI as Sg
import shared_vars as v
import virtual_display_controller as outD
import grid_controller as gc

from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

def draw_figure(canvas, figure):
    figure_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    figure_canvas_agg.draw()
    figure_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)
    return figure_canvas_agg


def runUI():
    button_layout = [[Sg.Text('Current Selected: (0,0)',key='selectedT'), Sg.Text('Current Mode: select', key='modeT'), Sg.Button('Build'), Sg.Button('Big Build'), Sg.Button('Build House'), Sg.Button('Create River'), Sg.Button('Dig'), Sg.Button('Select Mode'), Sg.Button('Reset Map'), Sg.Button('Close')]]
    mainLayout = [[Sg.B(' ', size=(2, 1), key=(i, j), button_color='gray') for i in range(v.max_x)] for j in range(v.max_y)]
    layout = [
        [Sg.Column(mainLayout, size=(400, 350), key='gridWindow'),Sg.Canvas(key='figCanvas',size=(200, 100))],
        [Sg.Column(button_layout, justification='right')]
    ]
    window = Sg.Window("app", layout)

    grid = gc.create_flat_grid()
    figAgg = False
    selected = [0, 0]

    mode = 'select'
    while True:
        event, values = window.read(timeout=10000)

        if event == 'Save Map':
            print ('save map')

        for i in range(v.max_x):
            for j in range(v.max_y):
                if event == (i, j):
                    window[selected[0], selected[1]].update(button_color='gray')
                    print ('pressed: ', i, ', ', j)
                    selected = [i, j]
                    window[event].update(button_color='red')
                    window['selectedT'].update('current selected: {}'.format(selected))


        if mode == 'river':
            for i in range(v.max_x):
                for j in range(v.max_y):
                    if event == (i, j):
                        print('pressed: ', i, ', ', j)
                        selected = [i, j]
                        window['selectedT'].update('current selected: {}'.format(selected))
                        grid = gc.create_river(grid, selected[0], selected[1])

        if event == 'Dig':
            grid = gc.dig(grid, selected[0], selected[1])

        if event == 'Build':
            grid = gc.build(grid, selected[0], selected[1])

        if event == 'Big Build':
            grid = gc.big_build(grid, selected[0], selected[1])

        if event == 'Build House':
            grid = gc.build_house(grid, selected[0], selected[1])

        if event == 'Create River':
            if mode == 'river':
                mode = 'select'
            else:
                mode = 'river'
            window['modeT'].update(mode)

        if event == 'Reset Map':
            grid = gc.create_flat_grid()

        if event == 'Select Mode':
            mode = 'select'
            window['modeT'].update(mode)

        if figAgg != False:
            figAgg.get_tk_widget().forget()
        fig, ax = outD.showTableState(grid)
        figAgg = draw_figure(window['figCanvas'].TKCanvas, fig)
        # exit run loop event
        if event == "Close" or event == Sg.WIN_CLOSED:
            break

        window.refresh()

    window.close()
