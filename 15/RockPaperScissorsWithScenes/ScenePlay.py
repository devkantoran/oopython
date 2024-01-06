# The Play scene
# The player chooses among rock, paper, or scissors

import pygwidgets
import pyghelpers
from Constants import *
import random
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
IMAGE_PATH = str(BASE_PATH) + "/images/"


class ScenePlay(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.RPSTuple = (ROCK, PAPER, SCISSORS)

        self.titleField = pygwidgets.DisplayText(
            self.window,
            (15, 40),
            "    Rock               Paper          Scissors",
            fontSize=50,
            textColor=WHITE,
            width=610,
            justified="center",
        )

        self.messageField = pygwidgets.DisplayText(
            self.window,
            (30, 395),
            "Choose!",
            fontSize=50,
            textColor=WHITE,
            width=610,
            justified="center",
        )

        self.rockButton = pygwidgets.CustomButton(
            self.window,
            (25, 120),
            up=IMAGE_PATH + "Rock.png",
            over=IMAGE_PATH + "RockOver.png",
            down=IMAGE_PATH + "RockDown.png",
        )

        self.paperButton = pygwidgets.CustomButton(
            self.window,
            (225, 120),
            up=IMAGE_PATH + "Paper.png",
            over=IMAGE_PATH + "PaperOver.png",
            down=IMAGE_PATH + "PaperDown.png",
        )

        self.scissorButton = pygwidgets.CustomButton(
            self.window,
            (425, 120),
            up=IMAGE_PATH + "Scissors.png",
            over=IMAGE_PATH + "ScissorsOver.png",
            down=IMAGE_PATH + "ScissorsDown.png",
        )

    def getSceneKey(self):
        return SCENE_PLAY

    def handleInputs(self, eventsList, keyPressedList):
        playerChoice = None

        for event in eventsList:
            if self.rockButton.handleEvent(event):
                playerChoice = ROCK

            if self.paperButton.handleEvent(event):
                playerChoice = PAPER

            if self.scissorButton.handleEvent(event):
                playerChoice = SCISSORS

            if playerChoice is not None:  # user has made a choice
                computerChoice = random.choice(self.RPSTuple)  # computer chooses
                dataDict = {"player": playerChoice, "computer": computerChoice}
                self.goToScene(SCENE_RESULTS, dataDict)  # go to Results scene

    # No need to include update method, defaults to inherited one which does nothing

    def draw(self):
        self.window.fill(GRAY)
        self.titleField.draw()
        self.rockButton.draw()
        self.paperButton.draw()
        self.scissorButton.draw()
        self.messageField.draw()
