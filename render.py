import pygame


def render(screen, map, LEFT, TOP, CELL_W, CELL_H):
    pygame.draw.rect(screen, [139, 69, 19], pygame.Rect(LEFT, TOP, CELL_W * 8, CELL_H * 8))

    pygame.draw.lines(
        screen,
        'black',
        True,
        [
            (LEFT, TOP),
            (LEFT + CELL_W * 8, TOP),
            (LEFT + CELL_W * 8, TOP + CELL_H * 8),
            (LEFT, TOP + CELL_H * 8)
        ],
        3
    )

    for row in map:
        for cell in row:
            cell.draw(screen)
