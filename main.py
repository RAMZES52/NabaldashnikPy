from render import render
from generate_map import generate_map
from generate_figure import generate_figure
import pygame

running = True
pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

TOP = int(height * 0.2)
LEFT = int(width * 0.35)

CELL_H = int((height * 0.55) / 8)
CELL_W = int((width * 0.30) / 8)

map = []

generate_map(map)

render(screen, map, LEFT, TOP, CELL_W, CELL_H)

figures = 0
current_figure = None

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                current_figure.move_figure(0, 1)
            elif event.key == pygame.K_w:
                current_figure.move_figure(0, -1)
            elif event.key == pygame.K_d:
                current_figure.move_figure(1, 0)
            elif event.key == pygame.K_a:
                current_figure.move_figure(-1, 0)
            elif event.key == pygame.K_SPACE:
                map, op = current_figure.place_figure(map)
                if op:
                    current_figure = None

    screen.fill([210, 105, 30])
    render(screen, map, LEFT, TOP, CELL_W, CELL_H)
    if current_figure:
        current_figure.draw(screen)
    else:
        figures += 1
        current_figure = generate_figure(figures, map)
    pygame.display.flip()
pygame.quit()
