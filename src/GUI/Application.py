import random
from tkinter import *
from tkinter import messagebox, filedialog
from tkinter.messagebox import showinfo
from GUI.Visualization import Visualization
from Helper.FilesManager import FilesManager
from Helper.Vector2D import Vector2D
from Simulation.Organisms.Plants.Hogweed import Hogweed
from Simulation.Organisms.Plants.Guarana import Guarana
from Simulation.Organisms.Plants.Dandelion import Dandelion
from Simulation.Organisms.Plants.Grass import Grass
from Simulation.Organisms.Plants.Belladonna import Belladonna
from Simulation.Organisms.Animals.Antelope import Antelope
from Simulation.Organisms.Animals.CyberSheep import CyberSheep
from Simulation.Organisms.Animals.Human import Human
from Simulation.Organisms.Animals.Fox import Fox
from Simulation.Organisms.Animals.Sheep import Sheep
from Simulation.Organisms.Animals.Wolf import Wolf
from Simulation.Organisms.Animals.Turtle import Turtle
from Simulation.World import World


class Application(Tk):
    TITLE = "Simulation"
    DEFAULT_HEIGHT = 600
    DEFAULT_WIDTH = 600

    def __init__(self, height, width):
        super().__init__()

        self._visualization = Visualization(
            self, int(Application.DEFAULT_HEIGHT * 9 / 10), self.__basedWorld()
        )
        self._filesManager = FilesManager()

        self.geometry(f"{width}x{height}")
        self.minsize(width, height)

        self.title(Application.TITLE)

        self.__initializeUpperMenu()

        self.__initializeMainPanel()

        self._visualization.paint()

    def __initializeUpperMenu(self):
        menuBar = Menu(self)
        menuNew = Menu(menuBar, tearoff=False)
        menuFile = Menu(menuBar, tearoff=False)

        menuNew.add_command(label="Start", command=self.__setBaseWorldVisualization)

        menuFile.add_command(label="Save", command=self.__saveWorldToFile)
        menuFile.add_command(label="Load", command=self.__loadWorldFromFile)

        menuBar.add_cascade(label="New Game", menu=menuNew)
        menuBar.add_cascade(label="File", menu=menuFile)

        self.config(menu=menuBar)

    def __initializeMainPanel(self):
        self._visualization.pack()

        buttonsPanel = PanedWindow()

        nextRoundButton = Button(
            buttonsPanel, text="Next Round", command=self.__nextRound
        )
        notificationsButton = Button(
            buttonsPanel, text="Notifications", command=self.__showNotifications
        )

        buttonsPanel.add(nextRoundButton)
        buttonsPanel.add(notificationsButton)
        buttonsPanel.pack()

    def __setBaseWorldVisualization(self):
        self._visualization.setWorld(self.__basedWorld())

    def __loadWorldFromFile(self):
        fileName = filedialog.askopenfilename()

        if fileName == "":
            return

        world = self._filesManager.load(fileName)

        if world is None:
            messagebox.showerror("Error", "Error in loading saved world")
            return

        self._visualization.setWorld(world)

    def __saveWorldToFile(self):
        fileName = filedialog.asksaveasfilename()

        if fileName == "":
            return

        self._filesManager.save(self._visualization.getWorld(), fileName)

    def __nextRound(self):
        self._visualization.nextRound()
        self._visualization.paint()

    def __showNotifications(self):
        notificationManager = (
            self._visualization.getNotificationManager().printOutNotifications()
        )
        showinfo("Notifications", notificationManager)

    def __basedWorld(self, type=World.Type.CARTESIAN):
        return World(
            20,
            20,
            [
                Fox(Vector2D(2, 2)),
                Fox(Vector2D(2, 3)),
                Fox(Vector2D(3, 2)),
                Fox(Vector2D(2, 1)),

                Wolf(Vector2D(5, 5)),
                Wolf(Vector2D(6, 5)),
                Wolf(Vector2D(5, 6)),
                
                
                Hogweed(Vector2D(10, 10)),
                Hogweed(Vector2D(19, 15)),
                
                CyberSheep(Vector2D(10, 15)),
                
            ],
            type,
        )

