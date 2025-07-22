import pygame
#import random

WIDTH =800
HEIGHT =600
FPS = 60

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
SKY_BLUE = (135,206,235)

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flappy fågel")
clock = pygame.time.Clock()

running = True
while running:
    # keep loop running at right fps
    clock.tick(FPS)

    #process input
    for event in pygame.event.get():
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # update

    #draw
    screen.fill(SKY_BLUE)
    #after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()


