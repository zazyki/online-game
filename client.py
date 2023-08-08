import pygame
from player import Player

width = 1000
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("jogo")
clock = pygame.time.Clock()


def draw(window, player):

    window.fill((255,255,255))
    player.draw(window)
    pygame.display.update()


def main():
    clock.tick(60)
    running= True
    p1 = Player(50,50,50,50,(0,0,0))
    while(running):
        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
                pygame.quit()
        p1.move()
        draw(window, p1)

main()