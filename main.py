import pygame

WIDTH = 1280
HEIGHT = 720

running = True

pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("purple")
    pygame.display.flip()

pygame.quit()
