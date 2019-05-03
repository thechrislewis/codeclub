#pygame code for creating circle sprites
import pygame, math, random
from circle import Circle

pygame.init()
        

def main():
    screen = pygame.display.set_mode((600,400))
    background = pygame.Surface((screen.get_size()))
    background.fill((150,150,150))
    background = background.convert()
           
    circleGRP = pygame.sprite.Group() #Add balls
    for x in range(10):
        circleGRP.add(Circle(screen))
   
    wind = pygame.math.Vector2(1.0, 0)
    gravity = pygame.math.Vector2(0, 0.1)
   
    clock = pygame.time.Clock()
    mainLoop = True
   
    while mainLoop:
        clock.tick(30) #Clock
        for event in pygame.event.get(): #Key events
            if event.type == pygame.QUIT:
                mainLoop = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    mainLoop = False
            elif event.type == pygame.MOUSEBUTTONDOWN: #Add wind
                if pygame.mouse.get_pressed()[0]:
                    for circle in circleGRP:
                        circle.applyForce(wind)
                   
#----------------------------------------------------------------------------                  
        for circle in circleGRP: #Add gravity
            gravity = gravity * circle.mass
            circle.applyForce(gravity)
            #pass
           
            #circleX = circle.dx * -1 #Add drag
            #circleY = circle.dy * -1
            #drag = (circleX/80* circle.mass* (circle.radius/5), circleY/80* circle.mass* (circle.radius/5))
            #circle.applyForce(drag)
       
#----------------------------------------------------------------------------    
        circleGRP.update()  
        screen.blit(background, (0,0))
        circleGRP.draw(screen)
        pygame.display.flip()
       
    pygame.quit()
       
if __name__ == "__main__":
    main()     
