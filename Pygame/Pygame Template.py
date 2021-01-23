# Template
import pygame
import random

WIDTH = 360
HEIGHT = 480
FPS = 30
#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

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
    screen.fill(RED)
    #only one place to draw the sprites to
    all_sprites.draw(screen)
    # ** After drawing everything, flip the display
    pygame.display.flip()