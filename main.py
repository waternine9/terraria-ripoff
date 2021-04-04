import pygame,sys,math,opensimplex
pygame.init()
from opensimplex import OpenSimplex

from defineID import *
def getSimplex(x,y,seed,simplex,idList,id):
    pixType = idList.get(id)
    threshold = pixType.genThreshold
    n = simplex.noise3d(x / pixType.spreadSimplex,y / pixType.spreadSimplex,seed)
    if n < threshold:
        return False
    else:
        return True

class pix:
    def __init__(self):
        self.id = 0
        self.pos = [0,0]
def main():
    display = pygame.display.set_mode((1000,1000))
    simplex = OpenSimplex()
    worldSize = [500,1000]
    map = [[0 for y in range(worldSize[1])] for x in range(worldSize[0])]
    seed = 127
    idList = getIdDefinitions()
    for x in range(worldSize[0]):
        n = simplex.noise2d(x / 10,seed) * 10 + 301
        n = round(n)
        b = 0
        for y in range(n,worldSize[1]):
            j = getSimplex(x,y,seed + 1,simplex,idList,1)
            if j:
                curPix = pix()
                curPix.id = 1
                map[x][y] = curPix
            else:
                curPix = pix()
                curPix.id = 2
                map[x][y] = curPix
    while True:
        display.fill((251,251,251))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()

                sys.exit()
        for y in range(worldSize[1]):
            for x in range(worldSize[0]):
                if map[x][y] != 0:
                    curPix = idList.get(map[x][y].id)
                    display.set_at((x,y),curPix.col)
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        quit()
                        sys.exit()
        pygame.display.update()
main()