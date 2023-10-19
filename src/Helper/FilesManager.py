import copy
from Helper.Vector2D import Vector2D
from Simulation.Organisms.Organism import Organism
from Simulation.Organisms.Plants.Hogweed import Hogweed
from Simulation.Organisms.Plants.Guarana import Guarana
from Simulation.Organisms.Plants.Dandelion import Dandelion
from Simulation.Organisms.Plants.Grass import Grass
from Simulation.Organisms.Plants.Belladonna import Belladonna
from Simulation.Organisms.Animals.Human import Human
from Simulation.Organisms.Animals.Antelope import Antelope
from Simulation.Organisms.Animals.CyberSheep import CyberSheep
from Simulation.Organisms.Animals.Fox import Fox
from Simulation.Organisms.Animals.Sheep import Sheep
from Simulation.Organisms.Animals.Wolf import Wolf
from Simulation.Organisms.Animals.Turtle import Turtle
from Simulation.World import World


class FilesManager:
    def __init__(self):
        pass

    def save(self, world: World, name: str):
        with open(name, "w") as out:
            out.write(
                f"{world.getRoundNumber()} {world.getHeight()} {world.getWidth()} {'CART'}\n"
            )

            for organism in world.getOrganisms():
                out.write(
                    f"{str(organism)} {organism.getAge()} {organism.getPosition().getY()} {organism.getPosition().getX()}"
                )

                if isinstance(organism, Human):
                    out.write(f" {organism.getSpecialAbilityCooldown()}")

                out.write("\n")

    def load(self, name):
        try:
            with open(name, "r") as input_file:
                lines = input_file.read().split("\n")
                lines = [line for line in lines if line.strip()]

                t, h, w, world_type = lines[0].split(" ")
                world = World(
                    int(h),
                    int(w),
                    None,
                    World.Type.HEX if world_type == "HEX" else World.Type.CARTESIAN,
                )
                world.setRoundNumber(int(t))

                for line in lines[1:]:
                    organism = self.__loadOrganism(line)
                    if organism:
                        world.addOrganism(organism)

                return world
        except Exception as e:
            print(f"Error while loading file: {e}")
            return None

    def __loadOrganism(self, line: str) -> Organism:
        args = line.split(" ")

        organism_name = args[0]
        organism = self.allocateOrganism(organism_name)

        if organism:
            organism.setAge(int(args[1]))
            organism.setPosition(Vector2D(int(args[2]), int(args[3])))

            if isinstance(organism, Human):
                organism.setSpecialAbilityCooldown(int(args[4]))

            return organism

        return None

    def allocateOrganism(self, name: str):
        position = Vector2D(0, 0)

        organisms = [
            Human(position),
            Wolf(position),
            Sheep(position),
            Fox(position),
            Turtle(position),
            Antelope(position),
            Grass(position),
            Dandelion(position),
            Guarana(position),
            Belladonna(position),
            Hogweed(position),
            CyberSheep(position),
        ]

        for organism in organisms:
            if str(organism) == name:
                return copy.deepcopy(organism)

        return None
