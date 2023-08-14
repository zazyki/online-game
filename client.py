import pygame
from player import Player
from network import Network

width = 1000
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("jogo")
clock = pygame.time.Clock()


def draw(window, player, player2, player3, player4):

    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    player3.draw(window)
    player4.draw(window)
    pygame.display.update()

def main():
    clock.tick(60)
    running= True
    nw = Network()

    p1 = nw.getRcv()
    p2 = Player(0,0,50,50,(0,0,0))
    p3 = Player(0,0,50,50,(0,0,0))
    p4 = Player(0,0,50,50,(0,0,0))

    while(running):
        players = nw.send(p1)
        p2 = players[0]
        p2.update()

        p3 = players[1]
        p3.update()

        p4 = players[2]
        p4.update()

        p1.move()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
            pygame.quit()
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
        draw(window, p1, p2, p3, p4)

main()