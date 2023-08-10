import pygame
from player import Player
from network import Network
from helpers import readPos, sendPos

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
    pos1 = readPos(nw.getPos())

    p1 = Player(pos1[0],pos1[1],50,50,(0,0,0))
    p2 = Player(0,0,50,50,(0,0,0))

    while(running):
        print(sendPos(p1.x, p1.y))
        pos2 = readPos(nw.send(sendPos(p1.x, p1.y)))
        p2.x = pos2[0]
        p2.y = pos2[1]
        p2.update()

        for event in pygame.event.get():
            if event == pygame.QUIT:
                running = False
                pygame.quit()
        p1.move()
        draw(window, p1, p2)

main()