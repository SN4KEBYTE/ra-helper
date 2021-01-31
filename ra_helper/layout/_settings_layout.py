import PySimpleGUI as sg

_GLOBAL_APPEARANCE_LAYOUT = [
    [
        sg.Text('Global Appearance'),
    ],
    [
        sg.InputOptionMenu(('Light', 'Dark')),
    ],
]

_HEATMAP_LAYOUT = [
    [
        sg.Text('Heatmap'),
    ],
    [
        sg.Text('kwargs dict (will override defaults params)'),
        sg.In('{}', key='-HMAP KWARGS-'),
    ],
    # [
    #     sg.Checkbox('Enable annotations', default=True, key='hmap-annotations'),
    # ],
    # [
    #     sg.Text('Format', size=(15, 1)),
    #     sg.In('.2g', key='-HMAP FMT-'),
    # ],
    # [
    #     sg.Text('Scale minimum', size=(15, 1)),
    #     sg.In('-1', key='-HMAP VMIN-'),
    # ],
    # [
    #     sg.Text('Scale maximum', size=(15, 1)),
    #     sg.In('1', key='-HMAP VMAX-'),
    # ],
    # [
    #     sg.Text('Scale center', size=(15, 1)),
    #     sg.In('1', key='-HMAP CENTER-'),
    # ],
    # [
    #     sg.Text('Form', size=(15, 1)),
    #     sg.InputOptionMenu(('Square', 'Lower triangle', 'Upper triangle'), key='-HMAP FORM-'),
    # ],
]

SETTINGS_LAYOUT = [
    [
        sg.Column(_GLOBAL_APPEARANCE_LAYOUT),
    ],
    [
        sg.HorizontalSeparator(),
    ],
    [
        sg.Column(_HEATMAP_LAYOUT),
    ],
]
