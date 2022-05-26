# Importing Libraries
import pygame
from pygame import mixer
pygame.init()

# Dimensions
WIDTH = 1400
HEIGHT = 800

# Color Scheme
black = (0,0,0)
white = (255,255,255)
gray = (128,128,128)

# Screen Dimensions
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Beat Mode")
label_font = pygame.font.Font("Roboto-Bold.ttf",32)

# FPS and Other Settings for screen
fps = 60
timer = pygame.time.Clock()


# Running the Beats!!
run = True
while run:
    timer.tick(fps)
    screen.fill(black)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()