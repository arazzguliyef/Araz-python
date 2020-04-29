import pygame 
import sys
import turtle

"""
def __init__(self, name, urgent=0):
        self.name = name
        exc_type, exc_msg = sys.exc_info()[:2]
        self.info = str(exc_msg)
        self.reason = "%s: %s" % (exc_type.__name__, self.info)
        self.urgent = urgent
        if urgent:
            self.warn()
"""
pygame.init()

win = pygame.display.set_mode( (500,500) )

pygame.display.set_caption("Firs Game")

x = 0
y = 452
width = 40
height = 40
vel = 5

isJump = False
jumpCount = 8

run = True
while run:
    pygame.time.delay(50)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()

    if keys [pygame.K_LEFT] and x > vel:
         x  -=  vel
    if keys [pygame.K_RIGHT] and x< 500 - width - vel:
        x +=vel
    if not (isJump):
        if keys [pygame.K_UP] and y > vel :
            y-=vel
        if keys [pygame.K_DOWN] and y < 500 -height - vel:
            y +=vel
        if keys [pygame.K_SPACE]:
            isJump = True    
   
    else:
        if jumpCount >= -8:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount **2) * 0.5 *neg
            jumpCount -= 1
         
        else:
            isJump = False
            jumpCount = 8

    win.fill((0,0,0))
    pygame.draw.rect(win, (255,0,0) , (x, y, width, height) )
    pygame.display.update()

pygame.quit()
