from Helper.Vector2D import Vector2D
from Simulation.Organisms.Organism import Organism
from Simulation.Organisms.Plant import Plant


class Guarana(Plant):
    STRENGTH = 0
    ADDITIONAL_STRENGTH = 3

    def __init__(self, position: Vector2D):
        super().__init__(position, Guarana.STRENGTH)

    def activateSpecialFeature(self, other: Organism):
        other.setStrength(other.getStrength() + Guarana.ADDITIONAL_STRENGTH)

    def draw(self) -> str:
        return "magenta"

    def __str__(self):
        return "GUARANA"
