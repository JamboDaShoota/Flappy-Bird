# Imports
import pygame
from pygame.locals import *
from pygame.image import load
import pygame.display as display
from bird_class import Bird

# Pygame initialization
pygame.init()

# Header statements
display.set_caption("Jambo's Flappy Bird")

# Image Loads

bg = load("assets/bg.png")
ground = load("assets/ground.png")

# Game Variables

    # Constants
clock = pygame.time.Clock()
fps = 60
screen_width = 864
screen_height = 936
        # set the screen var
screen = display.set_mode((screen_width, screen_height))

    # Dynamic Vars
ground_x = 0
ground_xoffset = 4
run = True
flappy = Bird(100, int(screen.get_height() / 2))
Bird.group.add(flappy)

flying = False
game_over = False

# Game Loop

while run:

    # draw the inital stuff
    clock.tick(fps)

    screen.blit(bg,(0,0))

    screen.blit(ground,(ground_x,bg.get_height()))

    Bird.group.draw(screen)
    if flying == True:
        Bird.group.update()

    if flappy.rect.bottom > 768:
        game_over = True
        flying = False

    if game_over == False:
        ground_x -= ground_xoffset
        if abs(ground_x) > 35:
            ground_x = 0
    for event in pygame.event.get():
        if event.type == QUIT:
            run = False

        if event.type ==  MOUSEBUTTONDOWN and flying == False:
            flying = True
    # update the screen constantly
    display.update()
pygame.quit()