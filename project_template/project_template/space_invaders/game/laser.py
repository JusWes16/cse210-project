from game.point import Point
from game import constants
import arcade
import random

class Laser(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.LASER_IMAGE)

        self.center_x = x
        self.center_y = y
        self.change_x = 0
        self.change_y = constants.LASER_SPEED
        

        