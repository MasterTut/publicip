import pygame

#Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 1
#dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

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

        newx = self.x + self.vx
        newy = self.y + self.vy

        if newx < BORDER+self.RADIUS:
            self.vx = -self.vy
        elif newy < BORDER+self.RADIUS or newy > HEIGHT-BORDER-self.RADIUS:
            self.vy = -self.vy


        else:
            self.show(bgcolor)
            self.x = self.x + self.vx
            self.y = self.y + self.vy
            self.show(fgcolor)
class Paddle:
    SHAPE = (20,20)
    def __init__(self,y):
        self.y = y
    def show(self, color):
        global screen
        pygame.draw.rect(screen, color,(WIDTH - 20,HEIGHT//2,10, 100))



#create objects

ballplay = Ball(WIDTH - Ball.RADIUS, HEIGHT//2, -VELOCITY, -VELOCITY)
paddleplay = Paddle(WIDTH)
# Draw the scenario
pygame.init()
fgcolor = pygame.Color("white")
bgcolor = pygame.Color("black")
red = pygame.Color("Red")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (WIDTH,BORDER))) #top
pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (BORDER, HEIGHT))) #left
pygame.draw.rect(screen, fgcolor, pygame.Rect(0,HEIGHT-BORDER, WIDTH, BORDER)) #bottom
#pygame.draw.rect(screen, fgcolor, pygame.Rect(WIDTH-BORDER,0,  BORDER, WIDTH)) # right
ballplay.show(fgcolor)
paddleplay.show(fgcolor)


def gameloop():
    running = True
    while running:
        pygame.display.flip()
        ballplay.update()


        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == K_c:
                    paddleplay.down = 0


gameloop()
