from random import randint


class Terrain:
    """
    生成地平线
    """

    def __init__(self, p1, p2):
        self.points = [p1, p2]

    def generate(self):
        self.h(self.points[0], self.points[1], 0)
        self.points.sort(key=lambda p: p[0])
        return self.points

    def h(self, p1, p2, deepth):
        limit = randint(2, 4)
        length = (p2[0] - p1[0]) // limit
        height = int(100 * pow(2, -deepth))
        if length <= 1:
            return
        p3 = (p1[0] + randint(1, limit - 1) * length, (p1[1] + p2[1]) // 2 + randint(-height, height))
        self.points.append(p3)
        self.h(p1, p3, deepth + 1)
        self.h(p3, p2, deepth + 1)


if __name__ == "__main__":
    import pygame
    pygame.init()
    surface = pygame.display.set_mode((1000, 500))

    ps = Terrain((0, 250), (1000, 250)).generate()
    ps.sort(key=lambda p: p[0])


    def draw():
        pre = ps[0]
        for p in ps:
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
