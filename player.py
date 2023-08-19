import pygame
from bullet import Bullet

class Player():
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = (x, y, width, height)
        self.xvel = 1
        self.yvel = 0
        self.facingRight = True
        self.cd = 500
        self.bullets = []

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.rect)
    
    def move(self):
        keys = pygame.key.get_pressed()
        self.yvel += 0.03
        if self.y >= 649:
                self.yvel = 0
        if keys[pygame.K_RIGHT] and self.x+self.width<=1000:
                self.x += self.xvel
                self.facingRight = True
        if keys[pygame.K_LEFT] and self.x>=0:
                self.x -= self.xvel
                self.facingRight = False
        if keys[pygame.K_UP] and self.y>=645:
                self.yvel -= 1

        if keys[pygame.K_x] and self.cd>=500:
                if self.facingRight:
                      self.bullets.append((self.x, self.y, 2))  
                else:
                      self.bullets.append((self.x, self.y, -2))
                self.cd = 0   
        self.update()

    def update(self):
          self.y += self.yvel
          self.cd += 1
          self.rect = (self.x, self.y, self.width, self.height)
