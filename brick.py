import pygame

BRICK_WIDTH = 100
BRICK_HEIGHT = 50

BRICK_COLOR = (255, 0, 0)
BRICK_TEXT_COLOR = (0, 0, 0)

class Brick:
    def __init__(self, lt_pos, count):
        self.rect = pygame.Rect(lt_pos[0], lt_pos[1], BRICK_WIDTH, BRICK_HEIGHT)
        self.initial_count = count
        self.count = count
    
    def draw(self, window):
        pygame.draw.rect(window, BRICK_COLOR, self.rect) 
        
        font = pygame.font.SysFont("Comic Sans MS", 30)
        text_surf = font.render("{}".format(self.count), True, (0, 0, 0))
        text_pos = (self.rect.centerx - text_surf.get_width() / 2 , self.rect.centery - text_surf.get_height() / 2)
        window.blit(text_surf, text_pos)  

    def update(self, window):
        pass     