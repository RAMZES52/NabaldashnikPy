from random import choice
from figure import Figure
from cell import Cell

colors = [
    (255, 255, 255), (0, 255, 0), (255, 0, 0), (0, 0, 255)
]


def generate_figure(id):
    color = choice(colors)
    shapes = [
        [Cell(0, 0, color), Cell(1, 0, color), Cell(0, 1, color), Cell(0, 2, color)],
        [Cell(0, 0, color), Cell(1, 0, color), Cell(2, 0, color), Cell(1, 1, color)],
        [Cell(0, 0, color), Cell(1, 0, color), Cell(1, 1, color), Cell(2, 1, color)],
        [Cell(0, 0, color), Cell(0, 1, color), Cell(0, 2, color)],
        [Cell(0, 0, color), Cell(1, 0, color), Cell(2, 0, color)],
        [Cell(0, 0, color), Cell(1, 0, color), Cell(0, 1, color), Cell(1, 1, color)],
        [Cell(0, 1, color), Cell(1, 0, color), Cell(1, 1, color), Cell(2, 1, color)],
        [Cell(0, 0, color), Cell(0, 1, color), Cell(1, 1, color), Cell(0, 2, color)],
        [Cell(1, 0, color), Cell(0, 1, color), Cell(1, 1, color), Cell(1, 2, color)]
    ]

    fig = Figure(id, choice(shapes))
    return fig


def can_place_figure(map, figure):
    for cell in figure.figure:
        x, y = cell.x_map, cell.y_map
        if not (0 <= x < 8 and 0 <= y < 8):
            return False
        if not map[x][y].is_free:
            return False
    return True


def generate_valid_figure(map, figures_count):
    max_attempts = 100  # Максимальное количество попыток
    attempts = 0

    while attempts < max_attempts:
        new_figure = generate_figure(figures_count)

        for x1 in range(8):
            for y1 in range(8):
                shifted_figure = Figure(new_figure.id_figure, *new_figure.figure)
                valid = True

                for i in shifted_figure.figure:
                    x, y = i.x_map + x1, i.y_map + y1
                    if not (0 <= x < 8 and 0 <= y < 8):
                        valid = False
                        break
                    if not map[x][y].is_free:
                        valid = False
                        break

                if valid:
                    for i in shifted_figure.figure:
                        i.move(x1, y1)
                    return shifted_figure

        attempts += 1

    raise KeyError
