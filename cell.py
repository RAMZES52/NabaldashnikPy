import pygame

pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

TOP = int(height * 0.2)
LEFT = int(width * 0.35)

CELL_H = int((height * 0.55) / 8)
CELL_W = int((width * 0.30) / 8)

pygame.quit()

class Cell:
    def __init__(self, x, y, color=None):
        self.x_map, self.y_map = x, y
        self.x = LEFT + self.x_map * CELL_W
        self.y = TOP + self.y_map * CELL_H
        self.color = color
        if color is None:
            self.is_free = True
        else:
            self.is_free = False

    def can_move(self, dx, dy):
        target_x, target_y = self.x_map + dx, self.y_map + dy
        if target_x > 7 or target_x < 0 or target_y > 7 or target_y < 0:
            return 0
        return 1

    def move(self, dx, dy):
        self.x_map, self.y_map = self.x_map + dx, self.y_map + dy
        self.x = LEFT + self.x_map * CELL_W
        self.y = TOP + self.y_map * CELL_H

    def can_change(self):
        if self.is_free:
            return 1
        return 0

    def change(self, color):
        self.color = color

    def draw(self, screen):
        rect = pygame.Rect(self.x, self.y, CELL_W, CELL_H)

        if self.color is not None:
            pygame.draw.rect(screen, self.color, rect)

        pygame.draw.rect(screen, "black", rect, 2)
