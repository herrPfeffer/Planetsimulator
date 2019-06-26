from PlanetManager import PlanetManager
from AnimatedScatter import AnimatedScatter

#create Manager instance
manager = PlanetManager(5)

#initialize variable number of planets
manager.CreatePlanet(description='planet1', xPosition=0, yPosition=1, mass=100000, x_speed=0.01, y_speed=0.01)
manager.CreatePlanet(description='planet2', xPosition=4, yPosition=2, mass=10, x_speed=0.01, y_speed=0.01)
manager.CreatePlanet(description='planet3', xPosition=2, yPosition=3, mass=10, x_speed=0.01, y_speed=0.01)
manager.CreatePlanet(description='planet4', xPosition=1, yPosition=4, mass=10, x_speed=0.01, y_speed=0.01)

#Show Planets in Plotter
scatter = AnimatedScatter("Planetsimulator", "x-Axis", "y-Axis", 2, manager)
