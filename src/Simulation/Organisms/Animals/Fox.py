from Helper.Vector2D import Vector2D
from Simulation.Organisms.Animal import Animal


class Fox(Animal):
    STRENGTH = 3
    INITIATIVE = 7

    def __init__(self, position: Vector2D):
        super().__init__(position, Fox.STRENGTH, Fox.INITIATIVE)

    def hasGoodSenseOfSmell(self):
        return True

    def draw(self) -> str:
        return "orange"

    def __str__(self):
        return "FOX"
