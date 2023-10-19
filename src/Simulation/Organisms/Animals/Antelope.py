from random import random
from Helper.Vector2D import Vector2D
from Simulation.Organisms.Animal import Animal


class Antelope(Animal):
    STRENGTH = 4
    INITIATIVE = 4
    REACH = 2
    CHANCE_TO_ESCAPE = 0.5

    def __init__(self, position: Vector2D):
        super().__init__(position, Antelope.STRENGTH, Antelope.INITIATIVE)

    def action(self):
        self._randomMove(Antelope.REACH)

    def isEscaped(self) -> bool:
        return random() < Antelope.CHANCE_TO_ESCAPE

    def draw(self) -> str:
        return "#964B00"

    def __str__(self):
        return "ANTELOPE"
