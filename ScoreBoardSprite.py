import pygame
import random
import math

class ScoreBoard(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.font = pygame.font.SysFont("None", 30)
        self.text = ""
        self.center = (0,0)
        self.image = self.font.render(self.text, 1, (255, 64, 0))
        self.rect = self.image.get_rect()
                
    def update(self):
        self.image = self.font.render(self.text, 1, (255, 64, 0))
        self.rect = self.image.get_rect()
        self.rect.center = self.center