import requests
import pygame
from pygame.locals import *

pygame.init()



#get public IP
def getip():
    response = requests.get('https://api.ipify.org/?format=unicode')
    results = response.content.decode('utf-8')
    return results


#create window
def drawwindow():
    pygame.display.set_caption('Public IP')
    surface = pygame.display.set_mode((200, 100))
    myfont = pygame.font.SysFont('Droid Sans', 30)
    textsurface = myfont.render(getip(), False, (255, 0, 0))
    surface.blit(textsurface,(0,0))
    pygame.display.flip()


# Game Loop
def gameloop():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        drawwindow()

gameloop()
