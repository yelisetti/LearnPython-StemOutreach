import pygame
import random
import time
from os import path

img_dir = path.join(path.dirname(__file__), "../imgs")

WIDTH = 480
HEIGHT = 600
FPS = 60

#colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rocket Shooter")
clock = pygame.time.Clock()

font_name = pygame.font.match_font('arial')
def draw_text(surf, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(player_img, (50, 40))
        self.image.set_colorkey(BLACK)
        # self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.radius = 20
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        self.speedx = 0
        self.speedy = 0

    def update(self):
        self.speedx = 0
        self.speedy = 0
        # list of the key presses
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            # print("Left_LEFT: {}".format(keystate[pygame.K_LEFT]))
            # print("Left_RIGHT: {}".format(keystate[pygame.K_RIGHT]))
            self.speedx = -5
        if keystate[pygame.K_RIGHT]:
            # print("RIGHT_LEFT: {}".format(keystate[pygame.K_LEFT]))
            # print("RIGHT_RIGHT: {}".format(keystate[pygame.K_RIGHT]))
            self.speedx = 5
        if keystate[pygame.K_UP]:
            # print("UP: {}".format(keystate[pygame.K_UP]))
            self.speedy = -5
        if keystate[pygame.K_DOWN]:
            # print("DOWN: {}".format(keystate[pygame.K_DOWN]))
            self.speedy = 5

        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT - 10
            # print(self.rect.top)
            # print("{}, {}".format(self.rect.x, self.rect.y))
        if self.rect.top < 0:
            self.rect.top = 0

    def shoot(self):
        bullet = Bullets(self.rect.centerx, self.rect.top)
        all_sprites.add(bullet)
        bullets.add(bullet)

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig = random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image = self.image_orig.copy()
        # self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width * .85/2)
        # pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        # position
        self.rect.x = random.randrange(0, WIDTH - self.rect.width)
        self.rect.y = random.randrange(-100, -40)
        # speed
        self.speedx = random.randrange(-3, 3)
        self.speedy = random.randrange(1, 8)
        # rotation
        self.rot = 0
        self.rot_speed = random.randrange(-8, 8)
        self.last_update = pygame.time.get_ticks()


    def rotate(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > 50:
            self.rot = (self.rot + self.rot_speed) % 360
            new_image = pygame.transform.rotate(self.image_orig, self.rot)
            old_center = self.rect.center
            self.image = new_image
            self.rect = self.image.get_rect()
            self.rect.center = old_center

    def update(self):
        self.rotate()
        self.rect.x = self.rect.x + self.speedx
        self.rect.y = self.rect.y + self.speedy
        if self.rect.top > HEIGHT + 10 or self.rect.left < -25 or self.rect.right > WIDTH + 20:
            self.rect.x = random.randrange(0, WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)


class Bullets(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(BLACK)
        # self.image.fill(YELLOW)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        self.rect.y = self.rect.y + self.speedy
        if self.rect.bottom < 0:
            self.kill()

# load all game graphics
player_img = pygame.image.load(path.join(img_dir, "playership.png")).convert()
# meteor_img = pygame.image.load(path.join(img_dir, "meteorBrown.png")).convert()
bullet_img = pygame.image.load(path.join(img_dir, "laserBlue.png")).convert()
meteor_images = []
meteor_list = ['meteorBrown_big1.png', 'meteorBrown_big2.png', 'meteorBrown_big3.png', 'meteorBrown_big4.png',
               'meteorBrown_med1.png', 'meteorBrown_med3.png', 'meteorBrown_small1.png', 'meteorBrown_small2.png']

for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir, img)).convert())

# Groups
all_sprites = pygame.sprite.Group()
mobs = pygame.sprite.Group()
bullets = pygame.sprite.Group()
userPlayer = Player()
all_sprites.add(userPlayer)
for i in range(8):
    m = Mob()
    all_sprites.add(m)
    mobs.add(m)
score = 0

startTime = time.time()
running = True
while running:
    clock.tick(FPS)
    # Processing input
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
            if event.key == pygame.K_SPACE:
                 userPlayer.shoot()
    # update
    all_sprites.update()

    hits = pygame.sprite.groupcollide(mobs, bullets, True, True)
    for hit in hits:
        score += 50 - hit.radius
        m = Mob()
        all_sprites.add(m)
        mobs.add(m)
    # check if player hits the mob, mob hits player
    # if hits, close the application
    hits_player = pygame.sprite.spritecollide(userPlayer, mobs, False, pygame.sprite.collide_circle)
    print(hits_player)
    if hits_player:
        running = False
        executionTime = time.time() - startTime
        print('Lasted for {} seconds'.format(executionTime))

    screen.fill(BLACK)
    # rendering
    all_sprites.draw(screen)
    draw_text(screen, "Score: {}".format(score), 24, WIDTH/2, 10)
    #double buffering
    pygame.display.flip()

pygame.quit()