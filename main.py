import pygame

WIDTH = 1920
HEIGHT = 1080

running = True

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Координаты левого верхнего угла поля
TOP = HEIGHT * 0.2
LEFT = WIDTH * 0.35
# Ширина и высота клетки
CELL_H = (HEIGHT * 0.55) / 8
CELL_W = (WIDTH * 0.30) / 8

map = list()


class Cell:
    def __init__(self, x, y, color=None):
        self.x = LEFT + x * CELL_W
        self.y = TOP + y * CELL_H
        self.color = color
        if color is None:
            self.status = True
        else:
            self.status = False

    def change(self, color):
        if self.status or (color is None):
            self.color = color
            return [0]
        else:
            return [1, self.status, color]


for i in range(8):
    a = list()
    for j in range(8):
        a.append(Cell(i, j, None))
    map.append(a)


def reder():
    # Отрисовка поля
    pygame.draw.rect(screen, [139, 69, 19], pygame.Rect(LEFT, TOP,
                                                        CELL_W * 8, CELL_H * 8))
    pygame.draw.lines(screen, 'black', True,
                      [(LEFT, TOP),
                       (LEFT + CELL_W * 8, TOP),
                       (LEFT + CELL_W * 8, TOP + CELL_H * 8),
                       (LEFT, TOP + CELL_H * 8)], 3)

    for row in map:
        for cel in row:
            if not cel.status:
                pygame.draw.rect(screen, cel.color, pygame.Rect(cel.x, cel.y, CELL_W, CELL_H + 1))

    for line in range(8):
        pygame.draw.line(screen, "black", (LEFT + (line * CELL_W), TOP),
                         (LEFT + (line * CELL_W), TOP + CELL_H * 8), 2)
        pygame.draw.line(screen, "black", (LEFT, TOP + line * CELL_H),
                         (LEFT + CELL_W * 8, TOP + line * CELL_H), 2)


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill([210, 105, 30])
    reder()
    pygame.display.flip()

pygame.quit()
