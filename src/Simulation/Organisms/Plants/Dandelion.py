from Helper.Vector2D import Vector2D
from Simulation.Organisms.Plant import Plant


class Dandelion(Plant):
    STRENGTH = 0
    CHANCES_TO_SPREAD = 3

    def __init__(self, position: Vector2D):
        super().__init__(position, Dandelion.STRENGTH)

    def action(self):
        for i in range(Dandelion.CHANCES_TO_SPREAD):
            self.spread()

    def draw(self) -> str:
        return "yellow"

    def __str__(self):
        return "DANDELION"
