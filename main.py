import pygame
import pygame.math as pgm
from math import pi
import movingObj as mob

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

gravity = pgm.Vector2(0,0.5)

 
# Set the height and width of the screen
size = [screenW, screenH]
screen = pygame.display.set_mode(size)
 
pygame.display.set_caption("Example1")
 
#Loop until the user clicks the close button.
done = False
clock = pygame.time.Clock()

obj = mob.movingObj(screenW/2,20,screenW, screenH)
 
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
    obj.show(screen)
    
    pygame.display.flip()
 
# Be IDLE friendly
pygame.quit()
