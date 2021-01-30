import PySimpleGUI as sg

_APPEARANCE_LAYOUT = [
    [
        sg.Text('Appearance'),
    ],
    [
        sg.InputOptionMenu(('Light', 'Dark')),
    ],
]

SETTINGS_LAYOUT = [
    [
        sg.Column(_APPEARANCE_LAYOUT),
    ],
    [
        sg.HorizontalSeparator(),
    ],
]
