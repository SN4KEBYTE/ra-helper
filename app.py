import PySimpleGUI as sg

from ra_helper.layout.layout import LAYOUT

window = sg.Window('RA Helper', LAYOUT)

while True:
    event, values = window.read()

    print(event, values, sep='\n')

    if event == 'OK' or event == sg.WIN_CLOSED:
        break

window.close()

# sg.theme_previewer()
