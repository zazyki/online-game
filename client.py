import pygame
from player import Player
from network import Network

width = 1000
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("jogo")
clock = pygame.time.Clock()


def draw(window, player, player2):

    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    pygame.display.update()

def main():
    clock.tick(60)
    running= True
    nw = Network()

    p1 = nw.getRcv()
    p2 = Player(0,0,50,50,(0,0,0))

    while(running):
        p2 = nw.send(p1)
        p2.update()

        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
                pygame.quit()
        p1.move()
        draw(window, p1, p2)

main()