from PlanetManager import PlanetManager
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

class AnimatedScatter(object):
    """An animated scatter plot using matplotlib.animations.FuncAnimation."""
    scats = []
    def __init__(self, title:str, x_label:str, y_label:str, legend:int, manager:PlanetManager):
        """Basic Constructor"""
        self.legend = legend
        self.manager = manager
        self.fig, self.ax = plt.subplots()
        self.ani = animation.FuncAnimation(self.fig, self.update, 
                                           interval=self.manager.timesteps, 
                                           init_func=self.setup_values, repeat=False)
        self.init_plotter(title, x_label, y_label)

    def init_plotter(self, title:str, xLabel:str, yLabel:str):
        """Intit the basic plotter and show it"""
        plt.title(title)
        self.fig.canvas.set_window_title(title)
        plt.xlabel(xLabel)
        plt.ylabel(yLabel)
        plt.show()

    def setup_values(self):
        """Setup the Scatter"""
        self.ax.set_xlim(right=self.manager.determine_max_x_position())
        self.ax.set_ylim(top=self.manager.determine_max_y_position())
        self.scats.clear()
        for planet in self.manager.planetary_objects:
            self.scats.append(self.ax.scatter(x=[], y=[], label=planet.description, alpha=0.5))
        self.ax.legend(loc=self.legend)
        return self.scats,

    def update(self, *args):
        """Update scatter values with the creator xPositions, yPositions methods"""
        counter = 0
        positionsMap = self.manager.get_positions()
        xPositions = positionsMap["xCoordinate"]
        yPositions = positionsMap["yCoordinate"]
        for scat in self.scats:
            scat.set_offsets(list(zip([xPositions[counter]], [yPositions[counter]])))
            counter += 1
        return self.scats,