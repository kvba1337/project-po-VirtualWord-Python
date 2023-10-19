import copy
from random import randint
from enum import Enum
from Helper.NotificationManager import NotificationManager
from Helper.Vector2D import Vector2D
from Simulation.Organisms.Organism import Organism


class World:
    class Type(Enum):
        CARTESIAN = (0,)
        HEX = 1

    class Move(Enum):
        UP = 0
        DOWN = 1
        LEFT = 2
        RIGHT = 3
        SPECIAL_ABILITY = 4
        STOP = 5

    def __init__(self, height, width, organisms=None, type=Type.CARTESIAN):
        if organisms is None:
            organisms = []
        else:
            for organism in organisms:
                organism.setWorld(self)

        self.__height = height
        self.__width = width
        self.__organisms = organisms
        self.__roundNumber = 0
        self.__notificationManager = NotificationManager()
        self.__move = World.Move.STOP
        self.__type = type

        print("New game started")
        self.getNotificationManager().addNotification("New game started")

    def getType(self):
        return self.__type

    def getHeight(self):
        return self.__height

    def getWidth(self):
        return self.__width

    def getNotificationManager(self):
        return self.__notificationManager

    def getOrganismAt(self, position: Vector2D) -> Organism:
        searchedOrganism = None

        for organism in self.__organisms:
            if organism.getPosition() == position and organism.isAlive():
                if (
                    searchedOrganism is None
                    or searchedOrganism.getStrength() < organism.getStrength()
                ):
                    searchedOrganism = organism

        return searchedOrganism

    def nextRound(self):
        self.__roundNumber += 1

        self.__notificationManager.clear()
        print(f"ROUND {self.__roundNumber}")
        self.getNotificationManager().addNotification("ROUND {}".format(self.__roundNumber))

        for org in self.__organisms:
            org.newRound()

        self.__organismsMove()
        self.__organisms = [x for x in self.__organisms if x.isAlive()]

    def addOrganism(self, org: Organism):
        org.setWorld(self)
        self.__organisms.append(org)

    def __organismsMove(self):
        self.__organisms = sorted(
            self.__organisms, reverse=True, key=lambda x: x.getAge()
        )
        self.__organisms = sorted(
            self.__organisms, reverse=True, key=lambda x: x.getInitiative()
        )

        for org in self.__organisms:
            if org.isAlive():
                org.action()
                org.collision()

            org.incrementAge()

    def getNewEmptyPlace(self, position: Vector2D, reach=1):
        for dy in [-1 * reach, 0, reach]:
            for dx in [-1 * reach, 0, reach]:
                newPosition = Vector2D(dy, dx) + position

                if (
                    newPosition != position
                    and self.getOrganismAt(newPosition) is None
                    and not newPosition.isOutOfBounds(self.getHeight(), self.getWidth())
                ):
                    return newPosition

        return position

    def getNewRandomEmptyPlace(self, position: Vector2D, reach=1):
        newPosition = []

        for dy in [-1 * reach, 0, reach]:
            for dx in [-1 * reach, 0, reach]:
                tempNewPosition = Vector2D(dy, dx) + position

                if (
                    tempNewPosition != position
                    and self.getOrganismAt(tempNewPosition) is None
                    and not tempNewPosition.isOutOfBounds(
                        self.getHeight(), self.getWidth()
                    )
                ):
                    newPosition.append(tempNewPosition)

        if len(newPosition):
            return newPosition[randint(0, len(newPosition) - 1)]

        return None

    def getOrganisms(self):
        return self.__organisms

    def getCollidingOrganism(self, organism):
        temp = [
            x
            for x in self.__organisms
            if x.getPosition() == organism.getPosition() and x != organism
        ]

        if len(temp):
            return temp[0]

        return None

    def setMove(self, move: Move):
        self.__move = move

    def popMove(self):
        currentMove = copy.deepcopy(self.__move)
        self.__move = World.Move.STOP

        return currentMove

    def getMove(self):
        return self.__move

    def getRoundNumber(self):
        return self.__roundNumber

    def setRoundNumber(self, roundNumber):
        self.__roundNumber = roundNumber
