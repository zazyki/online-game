import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    def __init__(self, x, y, vel):
        super(Bullet, self).__init__()
        self.x = x
        self.y = y
        self.vel = vel
        self.rect = (x, y, 10, 7)
        self.color = (0, 0, 0)

    def update(self):
          self.x += self.vel
          self.rect = (self.x, self.y, 10, 7)

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)