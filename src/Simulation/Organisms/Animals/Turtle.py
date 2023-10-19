from random import random
from Helper.Vector2D import Vector2D
from Simulation.Organisms.Organism import Organism
from Simulation.Organisms.Animal import Animal


class Turtle(Animal):
    STRENGTH = 2
    INITIATIVE = 1
    CHANCE_TO_MOVE = 0.25
    MAX_STRENGTH_TO_REFLECT_ATTACK = 5

    def __init__(self, position: Vector2D):
        super().__init__(position, Turtle.STRENGTH, Turtle.INITIATIVE)

    def action(self):
        if random() < Turtle.CHANCE_TO_MOVE:
            self._randomMove()

    def isAttackReflected(self, other: Organism) -> bool:
        return other.getStrength() < Turtle.MAX_STRENGTH_TO_REFLECT_ATTACK

    def draw(self) -> str:
        return "#438C7E"

    def __str__(self):
        return "TURTLE"
