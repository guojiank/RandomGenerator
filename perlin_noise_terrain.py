import noise
import random

"""
perlin noise 画一维地图
"""
if __name__ == "__main__":
    import pygame

    pygame.init()
    surface = pygame.display.set_mode((2000, 600))

    points = []
    sm = random.random()
    for i in range(2000):
        height = noise.pnoise1(sm) * 300 + 200
        points.append((i, height))
        sm += 0.005


    def draw():
        pre = points[0]
        for p in points:
            pygame.draw.line(surface, (255, 255, 255), pre, p)
            pre = p


    def controller():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()


    while True:
        controller()
        draw()
        pygame.display.flip()
