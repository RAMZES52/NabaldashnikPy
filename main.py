import time

from render import render
from generate_map import generate_map
from generate_figure import generate_figure
from button import Button
import pygame
from pprint import pprint


def kill():
    pygame.quit()
    exit()


def reverse_map(map):
    r_map = []
    for i in range(8):
        n = [map[j][i] for j in range(8)]
        r_map.append(n)
    return r_map


def check_score(map):
    for i in range(8):
        if all(cell.can_change() == 0 for cell in map[i]):
            for cell in map[i]:
                cell.change(None)
                cell.is_free = True
    r_map = reverse_map(map)
    for i in range(8):
        if all(cell.can_change() == 0 for cell in r_map[i]):
            for cell in r_map[i]:
                cell.change(None)
                cell.is_free = True

    return map


def main():
    map = []
    generate_map(map)
    render(screen, map, LEFT, TOP, CELL_W, CELL_H)

    figures = 0
    current_figure = None

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    kill()
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

        map = check_score(map)


def show_menu(screen):
    button_play = Button(180, 30, 360, 96, "Играть", main, (0, 0, 153))
    button_exit = Button(180, 156, 360, 96, "Выйти из игры", kill, (0, 0, 153))
    buttons = [button_play, button_exit]

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill()
            elif pygame.mouse.get_pressed()[0]:
                for i in buttons:
                    i.check()

        screen.fill([0, 102, 255])

        for i in buttons:
            i.draw(screen)

        pygame.display.flip()


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

TOP = int(height * 0.2)
LEFT = int(width * 0.35)

CELL_H = int((height * 0.55) / 8)
CELL_W = int((width * 0.30) / 8)

running = True

while running:
    show_menu(screen)
