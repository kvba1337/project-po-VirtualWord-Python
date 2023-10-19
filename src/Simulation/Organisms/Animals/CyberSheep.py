from Helper.Vector2D import Vector2D
from Simulation.Organisms.Plants.Hogweed import Hogweed
from Simulation.Organisms.Animal import Animal


class CyberSheep(Animal):
    STRENGTH = 11
    INITIATIVE = 4

    def __init__(self, position: Vector2D):
        super().__init__(position, CyberSheep.STRENGTH, CyberSheep.INITIATIVE)

    def action(self):
        nearestPosition = self.getPosition()

        for organism in self._world.getOrganisms():
            if isinstance(organism, Hogweed):
                hogweedPosition = organism.getPosition()
                if (
                    nearestPosition == self.getPosition()
                    or (nearestPosition - self.getPosition()).len()
                    > (hogweedPosition - self.getPosition()).len()
                ):
                    nearestPosition = hogweedPosition

        if nearestPosition == self.getPosition():
            super().action()
            return

        moveDirection = nearestPosition - self.getPosition()
        moveDirection = moveDirection.normalize()

        self._changePosition(moveDirection)

    def isImmuneToToxins(self) -> bool:
        return True

    def newRound(self):
        pass

    def draw(self) -> str:
        return "#7b68b0"

    def __str__(self):
        return "CYBER SHEEP"
