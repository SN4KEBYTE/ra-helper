import PySimpleGUI as sg

from ra_helper.layout._settings_layout import SETTINGS_LAYOUT
from ra_helper.layout._load_layout import LOAD_LAYOUT
from ra_helper.layout._heatmap_layout import HEATMAP_LAYOUT

LAYOUT = [
    [
        sg.TabGroup(
            [
                [
                    sg.Tab('Load', LOAD_LAYOUT),
                    # sg.Tab('View', _VIEW_LAYOUT),
                    # sg.Tab('Characteristics', _CHARACTERISTICS_LAYOUT),
                    # sg.Tab('Scatter plots', _SCATTER_LAYOUT),
                    sg.Tab('Heatmap', HEATMAP_LAYOUT, disabled=True),
                    sg.Tab('Settings', SETTINGS_LAYOUT),
                ]
            ]
        )
    ]
]