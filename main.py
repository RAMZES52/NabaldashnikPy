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

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, CELL_W, CELL_H)

        if self.color is not None:
            pygame.draw.rect(screen, self.color, rect)

        pygame.draw.rect(screen, "black", rect, 2)


for i in range(8):
    columns = []
    for j in range(8):
        columns.append(Cell(i, j, None))
    map.append(columns)


def render():
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


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill([210, 105, 30])
    render()
    pygame.display.flip()

pygame.quit()