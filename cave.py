import random
import copy


class Cave:
    def __init__(self):
        self.width = 100
        self.height = 100
        self.death_limit = 1
        self.birth_limit = 3
        self.init_number = 60
        print(f"{self.death_limit},{self.birth_limit},{self.init_number}")
        self.cave_map = self.init_map()

    def init_map(self):
        init_map = [[0 for i in range(self.height)] for j in range(self.width)]
        for i in range(self.width):
            for j in range(self.height):
                init_map[i][j] = 1 if random.randint(1, 101) > self.init_number else 0
        return init_map

    def gene(self):
        self.convert()

    def fill(self):
        for i in range(self.width):
            for j in range(self.height):
                neighbor = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 or y == 0:
                            continue
                        if 0 <= i + x < self.width and 0 <= j + y < self.height:
                            if self.cave_map[i + x][j + y] == 1:
                                neighbor += 1
                if self.cave_map[i][j] == 0:
                    if neighbor >= self.birth_limit:
                        self.cave_map[i][j] = 1
                else:
                    if neighbor <= self.death_limit:
                        self.cave_map[i][j] = 0

    def convert(self):
        old_map = self.cave_map
        rst_map = copy.deepcopy(old_map)
        for i in range(self.width):
            for j in range(self.height):
                neighbor = 0
                for x in range(-1, 2):
                    for y in range(-1, 2):
                        if x == 0 or y == 0:
                            continue
                        if 0 <= i + x < self.width and 0 <= j + y < self.height:
                            if old_map[i + x][j + y] == 1:
                                neighbor += 1
                if old_map[i][j] == 0:
                    if neighbor <= self.death_limit:
                        rst_map[i][j] = 0
                    else:
                        rst_map[i][j] = 1
                else:
                    if neighbor >= self.birth_limit:
                        rst_map[i][j] = 1
                    else:
                        rst_map[i][j] = 0

        self.cave_map = rst_map


if __name__ == "__main__":
    import pygame

    pygame.init()
    surface = pygame.display.set_mode((500, 500))

    cave = Cave()


    def draw():
        surface.fill([255, 255, 255])
        for i in range(cave.width):
            for j in range(cave.height):
                if cave.cave_map[i][j] == 1:
                    pygame.draw.rect(surface, (0, 0, 0), pygame.Rect(i * 5, j * 5, 5, 5), 0)
        pygame.display.flip()


    def controller():
        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
            if e.type == pygame.KEYDOWN:
                if e.key == pygame.K_SPACE:
                    cave.gene()


    while True:
        controller()
        draw()
