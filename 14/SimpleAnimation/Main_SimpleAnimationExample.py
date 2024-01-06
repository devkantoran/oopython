# Animation example
# Shows example of SimpleAnimation object

# 1 - Import library
import pygame
from pygame.locals import *
import sys
import pygwidgets
from SimpleAnimation import *

from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
IMAGE_PATH = str(BASE_PATH) + "/images/Dinobike/"


# 2 Define constants
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
FRAMES_PER_SECOND = 30
BGCOLOR = (0, 128, 128)

# 3 - Initialize the world
pygame.init()
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
clock = pygame.time.Clock()

# 4 - Load assets: images(s), sounds, etc.
dinosaurAnimTuple = (
    IMAGE_PATH + "f1.gif",
    IMAGE_PATH + "f2.gif",
    IMAGE_PATH + "f3.gif",
    IMAGE_PATH + "f4.gif",
    IMAGE_PATH + "f5.gif",
    IMAGE_PATH + "f6.gif",
    IMAGE_PATH + "f7.gif",
    IMAGE_PATH + "f8.gif",
    IMAGE_PATH + "f9.gif",
    IMAGE_PATH + "f10.gif",
)

# 5 - Initialize variables
oDinosaurAnimation = SimpleAnimation(window, (22, 140), dinosaurAnimTuple, 0.1)
oPlayButton = pygwidgets.TextButton(window, (20, 240), "Play")

# 6 - Loop forever
while True:
    # 7 - Check for and handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

        if oPlayButton.handleEvent(event):
            oDinosaurAnimation.play()

    # 8 - Do any "per frame" actions
    oDinosaurAnimation.update()

    # 9 - Clear the window
    window.fill(BGCOLOR)

    # 10 - Draw all window elements
    oDinosaurAnimation.draw()
    oPlayButton.draw()

    # 11 - Update the window
    pygame.display.update()

    # 12 - Slow things down a bit
    clock.tick(FRAMES_PER_SECOND)  # make pygame wait
