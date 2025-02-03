from render import render
from generate_map import generate_map
from generate_figure import generate_valid_figure
from check_score import check_score
from button import Button
import pygame


def kill():
    pygame.quit()
    exit()


def show_menu(screen):
    button_play = Button(600, 30, 720, 192, "Играть", main, (0, 0, 153), 64)
    button_exit = Button(600, 252, 720, 192, "Выйти из игры", kill, (0, 0, 153), 64)
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
        map = check_score(map)
        if current_figure is None:
            figures += 1
            try:
                current_figure = generate_valid_figure(map, figures)
            except Exception:
                player_name = get_player_name(screen)
                save_score(player_name, figures)
                kill()
        else:
            current_figure.draw(screen)
        pygame.display.flip()


def get_player_name(screen):
    font = pygame.font.Font(None, 64)
    input_box = pygame.Rect(width // 2 - 150, height // 2 - 32, 300, 64)
    color = (30, 144, 255)
    active = False
    text = ''
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kill()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        done = True
                    elif event.key == pygame.K_BACKSPACE:
                        text = text[:-1]
                    else:
                        text += event.unicode

        screen.fill([0, 102, 255])
        txt_surface = font.render(text, True, color)
        width_txt = max(300, txt_surface.get_width() + 10)
        input_box.w = width_txt
        screen.blit(txt_surface, (input_box.x + 5, input_box.y + 5))
        pygame.draw.rect(screen, color, input_box, 2)

        prompt_text = font.render("Введите ваше имя:", True, (255, 255, 255))
        screen.blit(prompt_text, (width // 2 - prompt_text.get_width() // 2, height // 2 - 100))

        pygame.display.flip()

    return text.strip()


def save_score(player_name, figures_count):
    with open("scores.txt", "a", encoding="utf-8") as file:
        file.write(f"{player_name}: {figures_count} фигурок\n")
    print(f"Результат сохранён: {player_name} - {figures_count} фигурок")


pygame.init()
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
width, height = screen.get_size()

TOP = int(height * 0.2)
LEFT = int(width * 0.35)

CELL_H = int((height * 0.55) / 8)
CELL_W = int((width * 0.30) / 8)

while True:
    show_menu(screen)
