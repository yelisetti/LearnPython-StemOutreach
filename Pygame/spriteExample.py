# Template
import pygame
import random
#will need to tell where the file is, not dependent on the computer we use
import os

WIDTH = 800
HEIGHT = 600
FPS = 30

#COLORS
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

# Setup folder for the assets - art/sound of the game
#Windows C:\Users\yelisev\PycharmProjects\PythonGUI\
#Windows C:\Users\yelisev\PycharmProjects\PythonGUI\img
#Mac:  C:/Users/yelisev/PycharmProjects/PythonGUI/
#Mac:  C:/Users/yelisev/PycharmProjects/PythonGUI/img
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, "img")

class Player(pygame.sprite.Sprite):
    # sprite for the player
    def __init__(self):
        # code will be run when a new player gets created
        # sprite wont function properly if not included
        pygame.sprite.Sprite.__init__(self)
        # just a image on the screen
        # self.image = pygame.Surface((50, 50))
        # filling the surface with a color
        # self.image.fill(RED)

        #using the image
        self.image = pygame.image.load(os.path.join(img_folder, "onlyrocket.png")).convert()
        #taking out the background color
        self.image.set_colorkey(BLACK)
        #converting the image to a smaller size
        self.image = pygame.transform.scale(self.image, (150, 150))
        # command to make sure the backgroud is transparent

        # define how tall and big they are
        self.rect = self.image.get_rect()
        #Tells us where and where we want it to be
        self.rect.center = (WIDTH/2, HEIGHT/2)
        self.y_speed = 5

    def update(self):
        # moving left to right by a speed of 5
        self.rect.x = self.rect.x + 5
        # means the y should have a bigger area as it goes to the bottom
        self.rect.y += self.y_speed
        # ensure that that sprite is constantly moving through the screen
        #reverse direction and go backwards
        if self.rect.bottom > HEIGHT - 200:
            self.y_speed = -5
        # same thing - in reverse of the top
        if self.rect.top < 200:
            self.y_speed = 5
        # Using the same width across the screen
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