import pygame

#Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 1

# define my classes

class Ball:
    RADIUS = 20
    def __init__(self,x,y,vx,vy):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
    def show(self, color):
        global screen
        pygame.draw.circle(screen, color, (self.x, self.y), self.RADIUS)
    def update(self):
        global bgcolor, fgcolor
        self.show(bgcolor)
        self.x = self.x + self.vx
        self.y = self.y + self.vy
        self.show(fgcolor)
class Paddle:
    pass

#create objects

ballplay = Ball(WIDTH - Ball.RADIUS, HEIGHT//2, -VELOCITY, 0)

# Draw the scenario
pygame.init()
fgcolor = pygame.Color("white")
bgcolor = pygame.Color("black")
red = pygame.Color("Red")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (WIDTH,BORDER)))
pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (BORDER, HEIGHT)))
pygame.draw.rect(screen, fgcolor, pygame.Rect(0,HEIGHT-BORDER, WIDTH, BORDER))
ballplay.show(fgcolor)


def gameloop():
    running = True
    while running:
        pygame.display.flip()
        ballplay.update()
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False


gameloop()
