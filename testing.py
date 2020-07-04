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
            if event.key == pygame.K_l:
                rect.left = 0
            if event.key == pygame.K_c:
                rect.centerx = width//2
            if event.key == pygame.K_r:
                rect.right = width
            if event.key == pygame.K_t:
                rect.top = 0
            if event.key == pygame.K_m:
                rect.centery = height//2
            if event.key == pygame.K_b:
                rect.bottom = height

            screen.fill(WHITE)

            pygame.draw.rect(screen, BLUE, rect)


            pygame.display.flip()

            pygame.quit()
