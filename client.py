import pygame
from pygame.sprite import Group
from network import Network

width = 1000
height = 700
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("jogo")
clock = pygame.time.Clock()

bullets = Group()

def draw(window, player, player2, player3, player4, bullets):

    window.fill((255,255,255))
    player.draw(window)
    player2.draw(window)
    player3.draw(window)
    player4.draw(window)

    for b in bullets:
        b.update()
        b.draw(window)
    pygame.display.update()

def main():
    clock.tick(60)
    running= True
    nw = Network()

    p1 = nw.getRcv()

    while(running):
        players = nw.send(p1)
        p2 = players[0]
        p2.update()

        p3 = players[1]
        p3.update()

        p4 = players[2]
        p4.update()

        bullets = players[3]
        p1.bullets = []
        p1.move()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            running = False
            pygame.quit()
        for event in pygame.event.get():
            if event == pygame.QUIT:
                pygame.quit()
        draw(window, p1, p2, p3, p4, bullets)

main()