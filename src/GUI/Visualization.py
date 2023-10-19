import math
from tkinter import *
from Helper.Vector2D import Vector2D
from Simulation.World import World


class Visualization(Canvas):
    __BACKGROUND_COLOR = "black"

    def __init__(self, master, windowHeight, world: World):
        self.__windowHeight = windowHeight
        self.__height = world.getHeight()
        self.__width = world.getWidth()

        self.__world = world

        self.__animalSize = int(self.__windowHeight / self.__height)

        super().__init__(
            master, height=windowHeight, width=self.__animalSize * self.__width
        )

        self.__events()

        self.focus_set()

    def paint(self):
        self.create_rectangle(
            0,
            0,
            self.__animalSize * self.__width,
            self.__animalSize * self.__height,
            fill=Visualization.__BACKGROUND_COLOR,
        )

        for y in range(self.__height):
            for x in range(self.__width):
                organism = self.__world.getOrganismAt(Vector2D(y, x))

                if organism is not None:
                    if self.__world.getType() == World.Type.CARTESIAN:
                        self.create_rectangle(
                            x * self.__animalSize,
                            y * self.__animalSize,
                            x * self.__animalSize + self.__animalSize,
                            y * self.__animalSize + self.__animalSize,
                            fill=organism.draw(),
                        )

                    else:
                        points = []

                        xtemp = x

                        if y % 2 == 0:
                            xtemp = x + 0.5

                        for i in range(0, 6):
                            xval = (
                                xtemp * self.__animalSize
                                + self.__animalSize / 2 * math.sin(i * 2 * math.pi / 6)
                            )
                            yval = (
                                y * self.__animalSize
                                + self.__animalSize / 2 * math.cos(i * 2 * math.pi / 6)
                            )

                            points.append(xval)
                            points.append(yval)

                        self.create_polygon(points, fill=organism.draw())

    def __events(self):
        def button(event):
            if event.keysym == "Up":
                self.__world.setMove(World.Move.UP)

            elif event.keysym == "Down":
                self.__world.setMove(World.Move.DOWN)

            elif event.keysym == "Left":
                self.__world.setMove(World.Move.LEFT)

            elif event.keysym == "Right":
                self.__world.setMove(World.Move.RIGHT)

            elif event.keysym == "r":
                self.__world.setMove(World.Move.SPECIAL_ABILITY)

            self.paint()

        self.bind("<Key>", button)

    def nextRound(self):
        self.__world.nextRound()

    def getNotificationManager(self):
        return self.__world.getNotificationManager()

    def setWorld(self, world: World):
        self.__world = world
        self.paint()

    def getWorld(self):
        return self.__world
