from Helper.Vector2D import Vector2D
from Simulation.Organisms.Animal import Animal


class Sheep(Animal):
    STRENGTH = 4
    INITIATIVE = 4

    def __init__(self, position: Vector2D):
        super().__init__(position, Sheep.STRENGTH, Sheep.INITIATIVE)

    def draw(self) -> str:
        return "gray"

    def __str__(self):
        return "SHEEP"
