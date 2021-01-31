import json
from pathlib import Path

import PySimpleGUI as sg

from ra_helper.layout.layout import LAYOUT
from ra_helper.data.utils import load_dataset
from ra_helper.plotting.defaults import HEATMAP_DEFAUTLS
from ra_helper.plotting.drawing import draw_figure
from ra_helper.plotting.heatmap import plot_heatmap

window = sg.Window('RA Helper', LAYOUT)

while True:
    event, values = window.read()

    if event == '-LOAD DATA-':
        # load dataset
        path = Path(values['-FOLDER-'])
        sep = values['-SEP-']
        has_header = values['ds-has-col-names']

        ds, cols = load_dataset(path, sep, has_header)

        # draw heatmap
        hmap_kwargs = {**HEATMAP_DEFAUTLS, **json.loads(values['-HMAP KWARGS-'])}
        fig = plot_heatmap(ds, **hmap_kwargs)
        fig_canvas_agg = draw_figure(fig, window['-HMAP CANVAS-'].TKCanvas)
        window.FindElement('Heatmap').Update(disabled=False)
    elif event == 'exit' or event == sg.WIN_CLOSED:
        break

window.close()

# sg.theme_previewer()
