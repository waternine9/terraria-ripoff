import pygame,sys,math,opensimplex
pygame.init()
from opensimplex import OpenSimplex

from defineID import *
def getSimplex(threshold,x,y,seed,simplex,idList,id):
    pixType = idList.get(id)

    n = simplex.noise3d(x / pixType.spreadSimplex,y / pixType.spreadSimplex,seed)
    if n < threshold:
        return 0
    else:
        return 1

class pix:
    def __init__(self):
        self.id = 0
        self.pos = [0,0]
def main():
    display = pygame.display.set_mode((1000,1000))
    simplex = OpenSimplex()
    map = [[0 for x in range(1000)] for y in range(1000)]
    seed = 1
    idList = getIdDefinitions()
    for x in range(1000):
        n = simplex.noise2d(x,seed) * 100 + 301
        n = round(n)
        for y in range(n,1000):
            j = 0
    while True:
        display.fill((251,251,251))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
                sys.exit()

        pygame.display.update()
main()