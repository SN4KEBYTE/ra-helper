import PySimpleGUI as sg

_PREPROCESSING_LAYOUT = [
    [
        sg.Text('Preprocessing'),
    ],
    [
        sg.Checkbox('Auto-drop NaN values', key='drop-nan'),
    ]
]

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
        sg.Column(_PREPROCESSING_LAYOUT),
    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        sg.Column(_APPEARANCE_LAYOUT),
    ],
    [
        sg.HorizontalSeparator(),
    ],
]
