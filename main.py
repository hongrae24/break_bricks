import pygame

from ball import Ball, BALL_RADIUS

WHITE = (255, 255, 255)

WINDOW_WIDTH = 500
WINDOW_HEIGHT = 700

pygame.init()
run = True

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Hello World")

ball = Ball(WINDOW_WIDTH / 2, WINDOW_HEIGHT - BALL_RADIUS)

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    window.fill(WHITE)

    ball.draw(window)

    pygame.display.update()

pygame.quit()
