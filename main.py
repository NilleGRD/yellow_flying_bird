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

def display_game_over():
    game_over_text = font.render("Game Over! Press SPACE to Restart", True, BLACK)
    screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 2))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('fågel.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, (60*2, 33*2))
        self.rect = self.image.get_rect()
        self.rect.center = ( int(WIDTH/2), int(HEIGHT/2) )
        self.speed = 0

    def update(self) -> bool:
        self.speed += 0.5
        self.rect.y += self.speed
        if self.rect.bottom > HEIGHT or self.rect.top < 0:
            return True
        else:
            return False

    def flap(self):
        self.speed -= 5

    def restart(self):
        self.rect.center = (int(WIDTH / 2), int(HEIGHT / 2))
        self.speed = 0


pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("flappy fågel")
clock = pygame.time.Clock()

# Font for timer
font = pygame.font.SysFont(None, 36)

# Start time in milliseconds
start_ticks = pygame.time.get_ticks()


all_sprites = pygame.sprite.Group()
player = Player()
#noinspection PyTypeChecker
all_sprites.add(player)

running = True
game_over = False

while running:
    # Calculate elapsed time in seconds
    seconds = (pygame.time.get_ticks() - start_ticks) // 1000

    # keep loop running at right fps
    clock.tick(FPS)

    #process input
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not game_over:
                    player.flap()
                else:
                    player.restart()
                    game_over = False
                    start_ticks = pygame.time.get_ticks()

        # check for closing window
        if event.type == pygame.QUIT:
            running = False

    # update
    if not game_over:
        game_over = player.update()

    #draw
    screen.fill(SKY_BLUE)
    all_sprites.draw(screen)

    # Render and draw the timer text
    timer_text = font.render(f"Time: {seconds}s", True, BLACK)
    screen.blit(timer_text, (10, 10))

    if game_over:
        display_game_over()

    #after drawing everything, flip the display
    pygame.display.flip()

pygame.quit()


