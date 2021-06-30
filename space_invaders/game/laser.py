from game.point import Point
from game import constants
import arcade
import random

class Laser(arcade.Sprite):
    def __init__(self, x, y, alien_laser = False):
        if alien_laser:
            super().__init__(constants.ALIEN_LASER_IMAGE)
            self.change_y = constants.ALIEN_LASER_SPEED
        else:
            super().__init__(constants.LASER_IMAGE)
            self.change_y = constants.LASER_SPEED
        
        self.center_x = x
        self.center_y = y
        self.change_x = 0
        

        