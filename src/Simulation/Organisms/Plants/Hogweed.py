from Helper.Vector2D import Vector2D
from Simulation.Organisms.Organism import Organism
from Simulation.Organisms.Plant import Plant
from Simulation.Organisms.Animal import Animal


class Hogweed(Plant):
    STRENGTH = 0

    def __init__(self, position: Vector2D):
        super().__init__(position, Hogweed.STRENGTH)

    def action(self):
        for y in range(-1, 2):
            for x in range(-1, 2):
                org = self._world.getOrganismAt(self.getPosition() + Vector2D(y, x))

                if isinstance(org, Animal) and not org.isImmuneToToxins():
                    org.kill()

        super().action()

    def activateSpecialFeature(self, other: Organism):
        if other.isImmuneToToxins():
            return

        other.kill()

    def draw(self) -> str:
        return "white"

    def __str__(self):
        return "HOGWEED"
