import pygame
import os
from personallib.camera import Camera
from personallib.canvas import *

# Constants
WIN_WIDTH = 800
WIN_HEIGHT = 800
FRAMERATE = 60
ICON_IMG = pygame.image.load(os.path.join("imgs", "icon.png"))

MAX_ITERATION = 100

# Pygame Setup
win = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("Mandelbrot Set")
pygame.display.set_icon(ICON_IMG)
clock = pygame.time.Clock()
pygame.font.init()

# Objects
cam = Camera(win, 0, 0, 1)
ui = Canvas(WIN_WIDTH, WIN_HEIGHT)

# Variables
running = True

# Methods


# UI



# Main Loop
if __name__ == '__main__':
    while running:
        
        clock.tick(FRAMERATE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                exit()
            
        win.fill((255, 255, 255))

        ui.update(cam)

        pygame.display.update()