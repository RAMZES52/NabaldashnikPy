import pygame


class Button:
    def __init__(self, x, y, w, h, text, func, color=(255, 255, 255), font_size=32):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.font = pygame.font.Font(None, 32)
        self.text = self.font.render(text, True, (255, 255, 255))
        self.func = func

    def check(self):
        mouse_pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(mouse_pos):
            self.func()

    def draw(self, screen):
        text_rect = self.text.get_rect(center=self.rect.center)
        pygame.draw.rect(screen, self.color, self.rect)
        screen.blit(self.text, text_rect)
