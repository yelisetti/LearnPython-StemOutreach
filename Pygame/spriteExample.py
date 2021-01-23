# Template
import pygame
import random

WIDTH = 800
HEIGHT = 600
FPS = 30
#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        # code will be run when a new player gets created
        # sprite wont function properly if not included
        pygame.sprite.Sprite.__init__(self)
        # just a image on the screen
        self.image = pygame.Surface((50, 50))
        # filling the surface with a color
        self.image.fill(RED)
        # define how tall and big they are
        self.rect = self.image.get_rect()
        #Tells us where and where we want it to be
        self.rect.center = (WIDTH/2, HEIGHT/2)

    def update(self):
        self.rect.x = self.rect.x + 5
        # ensure that that sprite is constantly moving through the screen
        if self.rect.left > WIDTH:
            self.rect.right = 0

# get the game to go
pygame.init()
# initializing the sound in the game
pygame.mixer.init()
# Creating the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Create the title of the window
pygame.display.set_caption("My First Game")
# Intializing the clock - handles the speed of the game
clock = pygame.time.Clock()

# add the sprites that you want to this group
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
# Game Loop
# Need to set a variable to ensure the game is running, if set to false, the game will end
running = True
while running:
    # keep running at the right speed - process the input, draw the screen (hopefully less than 1/30 second)
    # making sure the clock is running at the same speed
    # What if update takes slower than the fps you have it set to
    clock.tick(FPS)
    # Process input(events)
    # Events can happen at any time - happening at 1/30 of a second - DO NOT WANT TO SKIP KEY PRESSES
    for event in pygame.event.get():
        # Clicking the x in the window - close the window
        if event.type == pygame.QUIT:
            running = False
    # Update
    # entire group will update at once
    all_sprites.update()
    # Draw/render
    # IMPORTANT: when you have a lot of things you are doing(flying, enemies, shootings), you dont want to do it everytime - it is really slow
    # Double Buffering
    screen.fill(BLACK)
    #only one place to draw the sprites to
    all_sprites.draw(screen)
    # ** After drawing everything, flip the display
    pygame.display.flip()