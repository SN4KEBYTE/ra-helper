import PySimpleGUI as sg

from ra_helper.layout._settings_layout import SETTINGS_LAYOUT

LAYOUT = [
    [
        sg.TabGroup(
            [
                [
                    # sg.Tab('Load', _LOAD_LAYOUT),
                    # sg.Tab('View', _VIEW_LAYOUT),
                    # sg.Tab('Characteristics', _CHARACTERISTICS_LAYOUT),
                    # sg.Tab('Scatter plots', _SCATTER_LAYOUT),
                    sg.Tab('Settings', SETTINGS_LAYOUT),
                ]
            ]
        )
    ]
]