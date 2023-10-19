from random import random
from Helper.Vector2D import Vector2D
from Simulation.Organisms.Animal import Animal
from Simulation.Organisms.Animals.Antelope import Antelope
from Simulation.World import World


class Human(Animal):
    STRENGTH = 5
    INITIATIVE = 4
    SPECIAL_ABILITY_COOLDOWN = 6
    SPECIAL_ABILITY_COOLDOWN_SECOND_CHANCE = 2
    SPECIAL_ABILITY_PROPABILITY = 0.5

    def __init__(self, position: Vector2D):
        super().__init__(position, Human.STRENGTH, Human.INITIATIVE)
        self.__currentSpecialAbilityCooldown = -5

    def action(self):
        reach = 1

        if self.__currentSpecialAbilityCooldown <= 0:
            reach = 1
        elif (
            self.__currentSpecialAbilityCooldown
            > Human.SPECIAL_ABILITY_COOLDOWN_SECOND_CHANCE
        ):
            reach = Antelope.REACH
        else:
            if random() < Human.SPECIAL_ABILITY_PROPABILITY:
                reach = Antelope.REACH
            else:
                reach = 1

        move = self._world.popMove()

        if move == World.Move.UP:
            self._changePosition(Vector2D(reach * -1, 0))
        elif move == World.Move.DOWN:
            self._changePosition(Vector2D(reach, 0))
        elif move == World.Move.LEFT:
            self._changePosition(Vector2D(0, -1 * reach))
        elif move == World.Move.RIGHT:
            self._changePosition(Vector2D(0, reach))
        elif move == World.Move.SPECIAL_ABILITY:
            if self.__currentSpecialAbilityCooldown <= -5:
                self.__currentSpecialAbilityCooldown = Human.SPECIAL_ABILITY_COOLDOWN
                print("Special ability activated")
                self._world.getNotificationManager().addNotification("Special ability activated")
            else:
                print("Special ability is on cooldown")
                self._world.getNotificationManager().addNotification("Special ability is on cooldown")

        self.__currentSpecialAbilityCooldown -= 1

    def draw(self) -> str:
        return "#FFFD96"

    def __str__(self):
        return "HUMAN"

    def getSpecialAbilityCooldown(self):
        return self.__currentSpecialAbilityCooldown

    def setSpecialAbilityCooldown(self, cooldown):
        self.__currentSpecialAbilityCooldown = cooldown
