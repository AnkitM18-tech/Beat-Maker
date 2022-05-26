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

# FPS and Other Settings
fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6

# Grid drawing function
def draw_grid():
    # Menu boxes
    left_menu = pygame.draw.rect(screen,gray,[0,0,200,HEIGHT-200],5)
    bottom_menu = pygame.draw.rect(screen,gray,[0,HEIGHT-200,WIDTH,200],5)
    boxes = []
    colors = [gray,white,gray]
    # Left Box Instrument Menu
    hi_hat_text = label_font.render("Hi Hat",True,white)
    screen.blit(hi_hat_text,(30,30))
    snare_text = label_font.render("Snare",True,white)
    screen.blit(snare_text,(30,130))
    kick_text = label_font.render("Base Drum",True,white)
    screen.blit(kick_text,(30,230))
    crash_text = label_font.render("Crash",True,white)
    screen.blit(crash_text,(30,330))
    clap_text = label_font.render("Clap",True,white)
    screen.blit(clap_text,(30,430))
    floor_tom_text = label_font.render("Floor Tom",True,white)
    screen.blit(floor_tom_text,(30,530))
    for i in range(6):
        pygame.draw.line(screen,gray,(0, (i * 100) + 100),(200,(i * 100) + 100),3)
    for i in range(beats):
        for j in range(instruments):
            rect = pygame.draw.rect(screen,gray,[i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats), ((HEIGHT - 200) // instruments)],5,5)

# Running the Beats!!
run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    draw_grid()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.flip()
pygame.quit()