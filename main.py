import pygame
from pygame import Surface

#import random

WIDTH = 800
HEIGHT = 600
FPS = 30

#define colors
WHITE = (255,255,255)
BLACK = (0,0,0)
RED = (255,0,0)
GREEN = (0,255,0)
BLUE = (0,0,255)
YELLOW = (255,255,0)
SKY_BLUE = (135,206,235)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((100,100))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.center = ( int(WIDTH/2), int(HEIGHT/2) )
        self.speed = 0

    def update(self):
        self.speed += 0.1
        self.rect.y += self.speed
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            global running
            running = False

    def flap(self):
        self.speed -= 5

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flappy fågel")
clock = pygame.time.Clock()

all_sprites = pygame.sprite.Group()
player = Player()
#noinspection PyTypeChecker
all_sprites.add(player)

running = True
while running:
    # keep loop running at right fps
    clock.tick(FPS)
    #process input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.flap()
        # check for closing window
        if event.type == pygame.QUIT:
            running = False
    # update
    all_sprites.update()

    #draw
    screen.fill(SKY_BLUE)
    all_sprites.draw(screen)
    #after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()


