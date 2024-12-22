import pygame

BALL_COLOR = (0, 0, 255)
BALL_RADIUS = 13

class Ball:
    def __init__(self, x, y):
        self.pos = pygame.math.Vector2(x, y)
        self.move = pygame.math.Vector2(0, 0)
    
    def draw(self, window):
        pygame.draw.circle(window, BALL_COLOR, (self.pos.x, self.pos.y), BALL_RADIUS)
    
    def update(self):
        pass
