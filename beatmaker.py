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
green = (0,255,0)
gold = (212,175,55)
blue = (0,255,255)

# Screen Dimensions
screen = pygame.display.set_mode([WIDTH,HEIGHT])
pygame.display.set_caption("Beat Mode")
label_font = pygame.font.Font("Roboto-Bold.ttf",32)

# FPS and Other Settings
fps = 60
timer = pygame.time.Clock()
beats = 8
instruments = 6
bpm = 240
playing = True
boxes= []
clicked = [[-1 for _ in range(beats)] for _ in range(instruments)]
active_length = 0
active_beat = 1
beat_changed = True

# Loading Sounds
hi_hat = mixer.Sound("./sounds/hi hat.WAV")
snare = mixer.Sound("./sounds/snare.WAV")
kick = mixer.Sound("./sounds/kick.WAV")
crash = mixer.Sound("./sounds/crash.wav")
clap = mixer.Sound("./sounds/clap.wav")
floor_tom = mixer.Sound("./sounds/tom.WAV")
pygame.mixer.set_num_channels(instruments * 3)

# Play Notes Function
def play_notes():
    for i in range(len(clicked)):
        if clicked[i][active_beat] == 1:
            if i == 0:
                hi_hat.play()
            elif i == 1:
                snare.play()
            elif i == 2:
                kick.play()
            elif i == 3:
                crash.play()
            elif i == 4:
                clap.play()
            elif i == 5:
                floor_tom.play()
                
# Grid drawing function
def draw_grid(clicked,beat):
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
            if clicked[j][i] == -1:
                color = gray
            else:
                color = green
            rect = pygame.draw.rect(screen,color,[i * ((WIDTH - 200) // beats) + 205, (j * 100)+5, ((WIDTH - 200) // beats)-10, ((HEIGHT - 200) // instruments)-10],0,3)
            pygame.draw.rect(screen,gold,[i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats), ((HEIGHT - 200) // instruments)],5,5)
            pygame.draw.rect(screen,black,[i * ((WIDTH - 200) // beats) + 200, (j * 100), ((WIDTH - 200) // beats), ((HEIGHT - 200) // instruments)],2,5)
            boxes.append((rect,(i,j)))
        active = pygame.draw.rect(screen,blue,[beat * (WIDTH - 200) // beats + 200,0,((WIDTH - 200) // beats),instruments * 100],5,3)
    return boxes
    

# Running the Beats!!
run = True
while run:
    timer.tick(fps)
    screen.fill(black)
    boxes = draw_grid(clicked,active_beat)
    if beat_changed:
        play_notes()
        beat_changed = False
    # Clicked Beats Detection
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            for i in range(len(boxes)):
                if boxes[i][0].collidepoint(event.pos):
                    coords = boxes[i][1]
                    clicked[coords[1]][coords[0]] *= -1
    # Beat Tracker
    beat_length = 3600 // bpm
    if playing:
        if active_length < beat_length:
            active_length += 1
        else:
            active_length = 0
            if active_beat < beats - 1:
                active_beat += 1
                beat_changed = True
            else:
                active_beat = 0
                beat_changed = True

    pygame.display.flip()
pygame.quit()