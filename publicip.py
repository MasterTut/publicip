import requests
import pygame
from pygame.locals import *

pygame.init()
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)




#get public IP
def getip():
    return requests.get('https://api.ipify.org').text



#create window
def drawwindow(ip):
    pygame.display.set_caption('Public IP')
    surface = pygame.display.set_mode([250, 75], pygame.SRCALPHA)
    surface.fill(BLACK)
    myfont = pygame.font.SysFont('Droid Sans', 30)
    textsurface = myfont.render(ip, False, (204,255, 255))
    surface.blit(textsurface,(45,10))
def clock(fps):
    clock = pygame.time.Clock()
    clock.tick(fps)


# Game Loop
def gameloop():
    running = True
    while running:

        clock(60)
        drawwindow(getip())
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False



#testing



gameloop()
