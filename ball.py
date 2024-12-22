import pygame
import numpy as np

BALL_COLOR = (0, 0, 255)
BALL_RADIUS = 13

class Ball:
    def __init__(self, x, y):
        self.pos = np.array([x, y])
        self.move = np.array([0, 0])
    
    def draw(self, window):
        pygame.draw.circle(window, BALL_COLOR, (self.pos[0], self.pos[1]), BALL_RADIUS)
    
    def update(self):
        pass
