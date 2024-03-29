import math

class Planet():
    """Represents a planet"""
    
    def __init__(self, description:str, x_position:float, y_position:float, x_speed:float, y_speed:float, mass:float):
        """basic constructor to initialise a new planet with its attributes"""
        self.description = description
        self.x_position = x_position
        self.y_position = y_position
        self.x_speed = x_speed
        self.y_speed = y_speed
        self.mass = mass
       

    #the gravity constant which determines how the planets are influenced by each other
    gravity_constant = 6.67430*10**(-11)
    time = 10**5
    
    def move_next(self, planets:list, time):
        """move to the next timestep"""
        self.calculate_speed(planets, time)
        self.calculate_position(time)


    def calculate_speed(self, planetary_objects:list, time:int):
        """calculation of the new speed for the next timestep"""
        x_sum=0
        y_sum=0
        for planet in planetary_objects:
            if planet != self:
                x_sum+=((self.gravity_constant*planet.mass)/(math.sqrt((planet.x_position-self.x_position)**2+(planet.y_position-self.y_position)**2)**3))*(planet.x_position-self.x_position)
                y_sum+=((self.gravity_constant*planet.mass)/(math.sqrt((planet.x_position-self.x_position)**2+(planet.y_position-self.y_position)**2)**3))*(planet.y_position-self.y_position)
        self.x_speed+=self.time*x_sum           
        self.y_speed+=self.time*y_sum

    #time has to be increased because in realtime, the planets circle around the sun within one year
    def calculate_position(self, time):
        """calculation of the current position with the current speed"""
        self.x_position += 10**5 * self.x_speed
        self.y_position += 10**5 * self.y_speed

 