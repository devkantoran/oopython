#  PieView - Roll The Dice

import pygame
import pygame.gfxdraw
import math
import pygwidgets
from Constants import *

CENTER_X = 300
CENTER_Y = 300
RADIUS = 200
RADIUS_MINUS_1 = RADIUS - 1
BLACK = (0, 0, 0)


class PieView:
    def __init__(self, window, oModel):
        self.window = window
        self.oModel = oModel
        self.legendFieldsDict = {}
        y = 160
        # Create the legend fields
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            gray = (index * 20, index * 20, index * 20)
            oLegendField = pygwidgets.DisplayText(
                window, (550, y), value=str(index), fontSize=32, textColor=gray
            )
            self.legendFieldsDict[index] = oLegendField
            y = y + 25  # vertical spacing

    def update(
        self,
    ):
        nRounds, resultsDict, percentsDict = self.oModel.getRoundsRollsPercents()

        self.nRounds = nRounds
        self.resultsDict = resultsDict
        self.percentsDict = percentsDict
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            # Could use the count if we want to display it later
            # rollCount = resultsDict[index]
            percent = percentsDict[index]
            oLegendField = self.legendFieldsDict[index]

            # Build percent as a string with one decimal digit
            percent = "{:.1%}".format(percent)
            oLegendField.setValue(str(index) + ":   " + percent)

    def drawFilledArc(self, centerX, centerY, radius, degrees1, degrees2, color):
        """This method generates a list of points that are used to create
        a filled polygon representing an arc in the circle.  We'll use the
        angles passed in and a little trig to figure out the points in the arc
        """
        centerTuple = (centerX, centerY)
        nPointsToDraw = int(degrees2 - degrees1)
        if nPointsToDraw == 0:
            return  # nothing to draw
        # Both degrees parameters need to be converted to radians for calculating points
        radians1 = math.radians(degrees1)
        radians2 = math.radians(degrees2)
        radiansDiff = (radians2 - radians1) / nPointsToDraw

        # Start and end with the center point of the circle
        pointsList = [centerTuple]
        # Determine the points on the edge of the arc
        for pointNumber in range(nPointsToDraw + 1):
            offset = pointNumber * radiansDiff
            x = centerX + (radius * math.cos(radians1 + offset))
            y = centerY + (radius * math.sin(radians1 + offset))
            pointsList.append((x, y))
        pointsList.append(centerTuple)

        pygame.gfxdraw.filled_polygon(self.window, pointsList, color)
        # If you would like black lines around each arc, uncomment the next line
        # pygame.gfxdraw.polygon(self.window, pointsList, BLACK)

    # Draw the slice of the pie (arc) for every roll total
    def draw(self):
        startAngle = 0.0
        for index in range(MIN_TOTAL, MAX_TOTAL_PLUS_1):
            percent = self.percentsDict[index]
            endAngle = startAngle + (percent * 360)
            gray = (index * 20, index * 20, index * 20)
            self.drawFilledArc(
                CENTER_X, CENTER_Y, RADIUS_MINUS_1, startAngle, endAngle, gray
            )
            self.legendFieldsDict[index].draw()

            startAngle = endAngle  # set up for next wedge

        pygame.draw.circle(self.window, BLACK, (CENTER_X, CENTER_Y), RADIUS, 2)
