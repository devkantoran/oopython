# Splash scene - first scene the user sees
import pygwidgets
import pyghelpers
from Constants import *
from pathlib import Path

BASE_PATH = Path(__file__).resolve().parent
IMAGE_PATH = str(BASE_PATH) + "/images/"

class SceneSplash(pyghelpers.Scene):
    def __init__(self, window):
        self.window = window

        self.backgroundImage = pygwidgets.Image(
            self.window, (0, 0), IMAGE_PATH + "splashBackground.jpg"
        )
        self.dodgerImage = pygwidgets.Image(self.window, (150, 30), IMAGE_PATH + "dodger.png")

        self.startButton = pygwidgets.CustomButton(
            self.window,
            (250, 500),
            up=IMAGE_PATH + "startNormal.png",
            down=IMAGE_PATH + "startDown.png",
            over=IMAGE_PATH + "startOver.png",
            disabled=IMAGE_PATH + "startDisabled.png",
            enterToActivate=True,
        )

        self.quitButton = pygwidgets.CustomButton(
            self.window,
            (30, 650),
            up=IMAGE_PATH + "quitNormal.png",
            down=IMAGE_PATH + "quitDown.png",
            over=IMAGE_PATH + "quitOver.png",
            disabled=IMAGE_PATH + "quitDisabled.png",
        )

        self.highScoresButton = pygwidgets.CustomButton(
            self.window,
            (360, 650),
            up=IMAGE_PATH + "gotoHighScoresNormal.png",
            down=IMAGE_PATH + "gotoHighScoresDown.png",
            over=IMAGE_PATH + "gotoHighScoresOver.png",
            disabled=IMAGE_PATH + "gotoHighScoresDisabled.png",
        )

    def getSceneKey(self):
        return SCENE_SPLASH

    def handleInputs(self, events, keyPressedList):
        for event in events:
            if self.startButton.handleEvent(event):
                self.goToScene(SCENE_PLAY)
            elif self.quitButton.handleEvent(event):
                self.quit()
            elif self.highScoresButton.handleEvent(event):
                self.goToScene(SCENE_HIGH_SCORES)

    def draw(self):
        self.backgroundImage.draw()
        self.dodgerImage.draw()
        self.startButton.draw()
        self.quitButton.draw()
        self.highScoresButton.draw()
