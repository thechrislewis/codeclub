import pygame, math, random

       
class Circle(pygame.sprite.Sprite):
    def __init__(self, screen):
        pygame.sprite.Sprite.__init__(self)
        self.screen = screen
        self.position =  pygame.math.Vector2(random.randrange(20,self.screen.get_width()), self.screen.get_height()/3)
        self.velocity = pygame.math.Vector2(0.0, 0.0)
        self.acceleration = pygame.math.Vector2(0.0, 0.0)
        self.x = random.randrange(20,self.screen.get_width())
        self.y = self.screen.get_height()/2
        self.radius = random.randrange(5,30)
        self.image = pygame.Surface((self.radius*2,self.radius*2))
        self.image.set_colorkey((0,0,0))
        self.image.set_alpha(120)
        self.mass = self.radius/15.0
        pygame.draw.circle(self.image, (175,255,0), (self.radius,self.radius), self.radius)
        self.image = self.image.convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = self.position
       
    def update(self):
        self.calcPos()
        self.checkBounds()
        self.rect.center = self.position
       
    def calcPos(self):
        self.velocity += self.acceleration
        self.position += self.velocity
       
    def applyForce(self, force):
        self.acceleration += force
   
    def checkBounds(self):
        if self.position[1] > self.screen.get_height():
            self.acceleration[1] *= -1.0
            self.position[1] = self.screen.get_height()
        if self.position[0] > self.screen.get_width():
            self.acceleration[0] *= -1.0
            self.position[0] = self.screen.get_width()
        if self.position[1] < 0:
            self.acceleration[1] *= -1.0
        if self.position[0] < 0:
            self.acceleration[0] *= -1.0

