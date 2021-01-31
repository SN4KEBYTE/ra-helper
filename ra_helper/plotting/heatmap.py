import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


def plot_heatmap(df: pd.DataFrame, **kwargs):
    plt.tight_layout()

    corr = df.corr()

    fig, ax = plt.subplots(figsize=(10, 10))
    sns.heatmap(corr, **kwargs, ax=ax)

    return fig
