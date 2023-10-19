import copy
from random import random
from Helper.Vector2D import Vector2D
from Simulation.Organisms.Organism import Organism


class Plant(Organism):
    DEFAULT_INITIATIVE = 0
    CHANCE_TO_SPREAD = 0.05

    def __init__(self, position: Vector2D, strength):
        super().__init__(position, strength, Plant.DEFAULT_INITIATIVE)

    def action(self):
        self.spread()

    def collision(self):
        pass

    def newRound(self):
        pass

    def spread(self):
        if random() >= Plant.CHANCE_TO_SPREAD:
            return

        newPosition = self._world.getNewRandomEmptyPlace(self.getPosition())

        if newPosition is None:
            return

        org = copy.deepcopy(self)

        org.setAge(0)
        org.setPosition(newPosition)

        self._world.addOrganism(org)
