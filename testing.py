import pygame
from pygame.locals import *
WIDTH = 1200
HEIGHT = 600
RED = pygame.Color("Red")
BLUE = pygame.Color("Blue")
WHITE = pygame.Color("White")
pygame.init()
rect = pygame.Rect(50, 60, 200, 80)
running = True
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running =False

        if event.type == KEYDOWN:
            if event.key == pygame.K_LEFT:
                rect.left = 0
            

            screen.fill(WHITE)

            pygame.draw.rect(screen, BLUE, rect)


            pygame.display.flip()

            pygame.quit()
