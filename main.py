import pygame
import pygame.math as pgm
from math import pi

# Initialize the game engine
pygame.init()

# Define the colors we will use in RGB format
BLACK = (  0,   0,   0)
WHITE = (255, 255, 255)
BLUE =  (  0,   0, 255)
GREEN = (  0, 255,   0)
RED =   (255,   0,   0)

screenW = 640
screenH = 480

bounce = pgm.Vector2(1,-1)

gravity = pgm.Vector2(0,0.2)
drag = pgm.Vector2(0,-0.1)

class movingObj:

    def __init__(self, x,y):
        self.pos = pgm.Vector2(x,y)
        self.velocity = pgm.Vector2(0,0)
        self.acceleration = pgm.Vector2(0,0)
        self.w = 20
        self.h = 20
        self.colour = 0

    def checkBoundary(self):

        if (self.pos.y + self.velocity.y) > (screenH - self.h): 
            self.velocity.y = -self.velocity.y


    def update(self):
		
        self.checkBoundary()
        self.velocity += self.acceleration

        self.pos += self.velocity

        self.acceleration *= 0
		
    def applyForce(self, force): #forces accumulate before update 
        self.acceleration += force
		
    def show(self):
        pygame.draw.rect(screen, self.colour, [self.pos.x, self.pos.y, self.w, self.h], 1)

 
# Set the height and width of the screen
size = [screenW, screenH]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example1")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

obj = movingObj(screenW/2,20)
 
while not done:
 
    # This limits the while loop to a max of 10 times per second.
    # Leave this out and we will use all CPU we can.
    clock.tick(30)
     
    for event in pygame.event.get(): # User did something
        if event.type == pygame.QUIT: # If user clicked close
            done=True # Flag that we are done so we exit this loop
 
    # All drawing code happens after the for loop and but
    # inside the main while done==False loop.
     
    # Clear the screen and set the screen background
    screen.fill(WHITE)

    obj.applyForce(gravity)
     
    obj.update()
    obj.show()
    
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
