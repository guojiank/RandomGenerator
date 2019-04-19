import pygame
from generator import Terrain

pygame.init()
surface = pygame.display.set_mode((1000, 500))

ps = Terrain((0, 250), (1000, 250)).generate()
ps.sort(key=lambda p: p[0])


def draw():
    pre = ps[0]
    for p in ps:
        pygame.draw.line(surface, (255, 255, 255), pre, p)
        pre = p
    pass


def controller():
    for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
    pass


while True:
    controller()
    draw()
    pygame.display.flip()
