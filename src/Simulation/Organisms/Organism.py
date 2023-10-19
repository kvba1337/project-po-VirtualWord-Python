from abc import ABC, abstractmethod
from Helper.Vector2D import Vector2D


class Organism(ABC):
    def __init__(self, position: Vector2D, strength, initiative):
        self._world = None
        self._position = position
        self._strength = strength
        self._initiative = initiative
        self._isAlive = True
        self._age = 0

    def getPosition(self):
        return self._position

    def setPosition(self, position: Vector2D):
        self._position = position

    def getInitiative(self):
        return self._initiative

    def getStrength(self):
        return self._strength

    def setStrength(self, strength):
        self._strength = strength

    def getAge(self):
        return self._age

    def setAge(self, age):
        self._age = age

    def isAlive(self) -> bool:
        return self._isAlive

    def kill(self):
        self._world.getNotificationManager().addNotification(f"{str(self)} dies")
        self._isAlive = False
        print(f"{str(self)} dies")

    def activateSpecialFeature(self, other):
        pass

    def isAttackReflected(self, other) -> bool:
        return False

    def isImmuneToToxins(self) -> bool:
        return False

    def isEscaped(self) -> bool:
        return False

    def escape(self) -> bool:
        if self.isEscaped():
            newPosition = self._world.getNewEmptyPlace(self._position)

            if newPosition == self._position:
                return False

            self.setPosition(newPosition)

            return True

        return False

    def hasGoodSenseOfSmell(self):
        return False

    def incrementAge(self):
        self._age += 1

    def setWorld(self, world):
        self._world = world

    @abstractmethod
    def __str__(self):
        pass

    @abstractmethod
    def action(self):
        pass

    @abstractmethod
    def collision(self):
        pass

    @abstractmethod
    def draw(self) -> str:
        pass

    @abstractmethod
    def newRound(self):
        pass
