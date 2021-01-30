import PySimpleGUI as sg

_PREPROCESSING_LAYOUT = [
    [
        sg.Text('Preprocessing'),
    ],
    [
        sg.Checkbox('Auto-drop NaN values', key='drop-nan', default=True),
    ],
]

_PARAMS_LAYOUT = [
    [
        sg.Text('Params'),
    ],
    [
        sg.Checkbox('Dataset has column names', key='ds-has-col-names', default=True),
    ],
    [
        sg.Text('Separator:'),
        sg.In(',', key='-SEP-'),
    ],
]

_PATH_LAYOUT = [
    [
        sg.Text('Path'),
    ],
    [
        sg.In(size=(25, 1), enable_events=True, key='-FOLDER-'),
        sg.FileBrowse(file_types=(('Text Files', '*.txt'), ('CSV files', '*.csv'))),
    ],
]

LOAD_LAYOUT = [
    [
        sg.Column(_PREPROCESSING_LAYOUT),
    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        sg.Column(_PARAMS_LAYOUT),
    ],
    [
        sg.Column(_PATH_LAYOUT)
    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        sg.Button('Load', enable_events=True, key='-LOAD DATA-'),
    ],
]
