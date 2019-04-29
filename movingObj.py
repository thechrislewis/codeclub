import pygame
import pygame.math as pgm

class movingObj:

    def __init__(self, x,y):
        self.pos = pgm.Vector2(x,y)
        self.velocity = pgm.Vector2(0,0)
        self.acceleration = pgm.Vector2(0,0)
        self.w = 20
        self.h = 20
        self.colour = 0

    def checkBoundary(self):

        if (self.pos.y  > screenH: 
            self.pos.y = screenH
	    self.velocity.y *= -1
        
        if self.pos.x < 0:
            self.pos.x = 0
            self.velocity.x *= -1
        elif self.pos.x > screenX:
            self.pos.x = screenW
            self.velocity.x *= -1
	 
    def update(self):
		
        self.velocity += self.acceleration
        self.pos += self.velocity
        self.acceleration *= 0
        self.checkBoundary()	    
		
    def applyForce(self, force): #forces accumulate before update 
        self.acceleration += force
		
    def show(self):
        pygame.draw.rect(screen, self.colour, [self.pos.x, self.pos.y, self.w, self.h], 1)

