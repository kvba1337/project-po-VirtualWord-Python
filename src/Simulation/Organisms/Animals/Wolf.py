from Helper.Vector2D import Vector2D
from Simulation.Organisms.Animal import Animal


class Wolf(Animal):
    STRENGTH = 9
    INITIATIVE = 5

    def __init__(self, position: Vector2D):
        super().__init__(position, Wolf.STRENGTH, Wolf.INITIATIVE)

    def draw(self) -> str:
        return "red"

    def __str__(self):
        return "WOLF"
