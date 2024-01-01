# New Years Countdown!
import os
import random

import pygame

def draw_confetti(screen, colors):
    for _ in range(20):
        x = random.randint(0, screen.get_width())
        y = random.randint(0, screen.get_height())
        color = random.choice(colors)
        pygame.draw.circle(screen, color, (x, y), 5)

def countdown_timer(seconds: int):
    # Constants
    pygame.init()
    # screen = pygame.display.set_mode((800, 600))
    screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
    pygame.display.set_caption("New Year's Countdown")
    screen_w = screen.get_width()
    screen_h = screen.get_height()
    red = (255, 0, 0)
    green = (0, 255, 0)
    blue = (0, 0, 255)
    orange = (255, 165, 0)
    pink = (255, 192, 203)
    white = (255, 255, 255)
    black = (0, 0, 0)
    colors = [red, green, blue, orange, pink]
    font = pygame.font.Font(None, 106)

    # Countdown
    for sec in range(seconds, 0, -1):
        bg_color = random.choice(colors)
        screen.fill(bg_color)
        text = font.render(str(sec), True, black)
        screen.blit(
            text,
            (
                (screen_w // 2) - text.get_width() // 2,
                (screen_h // 2) - text.get_height() // 2
            )
        )

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                pygame.quit()
                os.sys.exit(0)

        pygame.time.delay(1000)


    # TIME IS UP!
    screen.fill(white)
    new_years_text = font.render("Happy New Year's", True, red)
    screen.blit(
                new_years_text,
                (
                    (screen_w // 2) - new_years_text.get_width() // 2,
                    (screen_h // 2) - new_years_text.get_height() // 2
                )
            )
    
    year_text = font.render("2024", True, red)
    screen.blit(
                year_text,
                (
                    (screen_w // 2) - year_text.get_width() // 2,
                    ((screen_h // 2) - year_text.get_height() // 2) + 100
                )
            )
    draw_confetti(screen, colors)

    pygame.display.flip()

    is_running = True
    while is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT or (
                event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE
            ):
                is_running = False


    pygame.quit()


if __name__ == "__main__":
    countdown_timer(10)