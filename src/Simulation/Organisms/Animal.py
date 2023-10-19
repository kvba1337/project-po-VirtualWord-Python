import copy
from random import randint
from Helper.Vector2D import Vector2D
from Simulation.Organisms.Organism import Organism


class Animal(Organism):
    def __init__(self, position: Vector2D, strength, initiative):
        super().__init__(position, strength, initiative)
        self._isCloned = False

    def action(self):
        self._randomMove()

    def collision(self):
        collidingOrganism = self._world.getCollidingOrganism(self)

        if collidingOrganism is None:
            return

        if str(collidingOrganism) == str(self):
            self._clone(collidingOrganism)
            return

        self._fight(collidingOrganism)

    def newRound(self):
        self._isCloned = False

    def _randomMove(self, reach=1):
        if self.hasGoodSenseOfSmell() and self.isEveryNeighBorStronger():
            return

        coordinates = [-1 * reach, 0, reach]
        previousPosition = Vector2D(self._position.getY(), self._position.getX())

        while True:
            randX = coordinates[randint(0, 2)]
            randY = coordinates[randint(0, 2)]

            newPosition = Vector2D(randY, randX)

            self._changePosition(newPosition)

            if not (
                previousPosition == self._position
                or (
                    self.hasGoodSenseOfSmell()
                    and self._world.getCollidingOrganism(self) is not None
                    and self._world.getCollidingOrganism(self).getStrength()
                    > self.getStrength()
                )
            ):
                break

    def _changePosition(self, newPosition: Vector2D):
        if self._world.getType() and (
            newPosition == Vector2D(-1, -1) or newPosition == Vector2D(1, -1)
        ):
            return

        if not (self.getPosition() + newPosition).isOutOfBounds(
            self._world.getHeight(), self._world.getWidth()
        ):
            self._previousPosition = Vector2D(
                self._position.getY(), self._position.getX()
            )
            self._position += newPosition

    def _clone(self, collidingOrganism):
        if collidingOrganism.getAge() == 0:
            return

        organism = copy.deepcopy(self)
        self.__moveBack()

        newPosition = self._world.getNewEmptyPlace(collidingOrganism.getPosition())

        if (
            newPosition == collidingOrganism.getPosition()
            or collidingOrganism._isCloned
            or self._isCloned
        ):
            return

        organism.setPosition(newPosition)
        organism.setAge(-1)

        self._world.addOrganism(organism)

        self._isCloned = True
        collidingOrganism._isCloned = True

    def __moveBack(self):
        self.setPosition(self._previousPosition)

    def _fight(self, collidingOrganism: Organism):
        if self.escape() or collidingOrganism.escape():
            return

        if self.getStrength() < collidingOrganism.getStrength():
            if self.isAttackReflected(collidingOrganism):
                self.__moveBack()
                return

            self._world.getNotificationManager().addNotification(
                f"{str(collidingOrganism)} kills {str(self)}"
            )
            print(f"{str(collidingOrganism)} kills {str(self)}")
            self.kill()
            self.activateSpecialFeature(collidingOrganism)

            return

        if collidingOrganism.isAttackReflected(self):
            self.__moveBack()
            return

        self._world.getNotificationManager().addNotification(
            f"{str(self)} kills {str(collidingOrganism)}"
        )
        print(f"{str(self)} kills {str(collidingOrganism)}")
        collidingOrganism.kill()
        collidingOrganism.activateSpecialFeature(self)

    def isEveryNeighBorStronger(self) -> bool:
        for y in range(-1, 2):
            for x in range(-1, 2):
                position = Vector2D(y, x)

                organism = self._world.getOrganismAt(self.getPosition() + position)

                if organism != self and (
                    organism is None or organism.getStrength() <= self.getStrength()
                ):
                    return False

        return True
