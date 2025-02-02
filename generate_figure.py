from random import choice
from figure import Figure
from cell import Cell

colors = [
    (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255)
]


def generate_figure(id, map):
    color = choice(colors)
    shapes = [
        [Cell(0, 0, color), Cell(1, 0, color), Cell(2, 0, color), Cell(1, 1, color)],
        [Cell(0, 0, color), Cell(0, 1, color), Cell(0, 2, color), Cell(1, 0, color)],
    ]
    shape = choice(shapes)
    fig = Figure(id, *shape)
    return fig
