import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 500, 500
WHITE = (255, 255, 255)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Sprite Color Change Event")

# Define a custom event
CHANGE_COLOR_EVENT = pygame.USEREVENT + 1
pygame.time.set_timer(CHANGE_COLOR_EVENT, 2000)  # Change color every 2 seconds

# Sprite class
class ColoredSprite(pygame.sprite.Sprite):
    def __init__(self, x, y, size=50):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.color = self.random_color()
        self.image.fill(self.color)
        self.rect = self.image.get_rect(center=(x, y))
    
    def random_color(self):
        return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    
    def change_color(self):
        self.color = self.random_color()
        self.image.fill(self.color)

# Create sprite instances
sprite1 = ColoredSprite(150, 250)
sprite2 = ColoredSprite(350, 250)

# Sprite group
all_sprites = pygame.sprite.Group(sprite1, sprite2)

# Game loop
running = True
while running:
    screen.fill(WHITE)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == CHANGE_COLOR_EVENT:
            sprite1.change_color()
            sprite2.change_color()
    
    all_sprites.draw(screen)
    pygame.display.flip()
    
    pygame.time.delay(100)

pygame.quit()
