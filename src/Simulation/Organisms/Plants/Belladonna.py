from Helper.Vector2D import Vector2D
from Simulation.Organisms.Organism import Organism
from Simulation.Organisms.Plant import Plant


class Belladonna(Plant):
    STRENGTH = 0

    def __init__(self, position: Vector2D):
        super().__init__(position, Belladonna.STRENGTH)

    def activateSpecialFeature(self, other: Organism):
        other.kill()

    def draw(self) -> str:
        return "#31004C"

    def __str__(self):
        return "BELLADONNA"
