import pygame

#Variables
WIDTH = 1200
HEIGHT = 600
BORDER = 20
VELOCITY = 1
MOVE = 0


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

    def __init__(self,y):
        self.y = y

    def show(self, color):
        global screen
        pygame.draw.rect(screen, color,(WIDTH - 20, self.y,10, 100))
    def update(self, v):
        global MOVE
        self.show(bgcolor)
        self.y = self.y + v


        self.show(fgcolor)

        if self.y == HEIGHT - (100 + BORDER) or self.y == 0 + BORDER:
            MOVE = 0


#create objects

ballplay = Ball(WIDTH - (Ball.RADIUS + 20), HEIGHT//2, -VELOCITY, -VELOCITY)
paddleplay = Paddle(HEIGHT//2)
# Draw the scenario
pygame.init()
fgcolor = pygame.Color("white")
bgcolor = pygame.Color("black")
red = pygame.Color("Red")
screen = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (WIDTH,BORDER))) #top
pygame.draw.rect(screen, fgcolor, pygame.Rect((0,0), (BORDER, HEIGHT))) #left
pygame.draw.rect(screen, fgcolor, pygame.Rect(0,HEIGHT-BORDER, WIDTH, BORDER)) #bottom

ballplay.show(fgcolor)
paddleplay.show(fgcolor)
def youlose():
    myfont = pygame.font.SysFont('Droid Sans', 100)
    youlose = myfont.render('You Lose', False, (fgcolor))
    screen.blit(youlose, (WIDTH//2 - 100,HEIGHT//2))

def gameloop():
    global MOVE
    running = True
    while running:

        pygame.display.flip()

        ballplay.update()
        paddleplay.update(MOVE)





        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN and paddleplay.y != 480:
                    MOVE = MOVE + 1

                if event.key == pygame.K_UP and paddleplay.y != 20:
                    MOVE = MOVE - 1
                if event.key == pygame.K_RIGHT:
                    MOVE = 0


            if ballplay.y >= paddleplay.y + 25 and ballplay.x >= 1200:
                ballplay.vx = +ballplay.vy
            elif ballplay.x >= 1200:
                youlose()





gameloop()
