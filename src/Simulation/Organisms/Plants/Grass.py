from Helper.Vector2D import Vector2D
from Simulation.Organisms.Plant import Plant


class Grass(Plant):
    STRENGTH = 0

    def __init__(self, position: Vector2D):
        super().__init__(position, Grass.STRENGTH)

    def draw(self) -> str:
        return "green"

    def __str__(self):
        return "GRASS"
