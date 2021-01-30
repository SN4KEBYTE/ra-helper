from pathlib import Path

import PySimpleGUI as sg
import pandas as pd


def load_dataset(path: Path, sep: str, has_header: bool) -> tuple[pd.DataFrame, list[str]]:
    kwargs = {'sep': sep}

    if not has_header:
        kwargs['header'] = None

    ds = pd.read_csv(path, **kwargs)

    if has_header:
        ds = ds[1:]
    else:
        ds.columns = [f'col{i}' for i in range(len(ds.shape[1]))]

    return ds, list(ds.columns)


def show_dataset(ds: pd.DataFrame, header: list[str]):
    return [
        [
            sg.Table(values=ds.values.tolist(), headings=header, display_row_numbers=False, auto_size_columns=True,
                     num_rows=min(25, ds.shape[0])),
        ]
    ]


def show_stats(df: pd.DataFrame):
    stats = df.describe().T
    headings = list(stats.columns)
    data = stats.values.tolist()

    for i, d in enumerate(data):
        d.insert(0, list(stats.index)[i])

    headings = ['Feature'] + headings

    return [
        [
            sg.Table(values=data, headings=headings, font='Consolas', display_row_numbers=False, auto_size_columns=True,
                     num_rows=min(25, len(data)))
        ]
    ]
