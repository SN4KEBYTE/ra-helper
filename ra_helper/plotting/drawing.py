from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def draw_figure(figure, canvas):
    fig_canvas_agg = FigureCanvasTkAgg(figure, canvas)
    fig_canvas_agg.draw()
    fig_canvas_agg.get_tk_widget().pack(side='top', fill='both', expand=1)

    return fig_canvas_agg
