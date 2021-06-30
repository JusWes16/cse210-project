from game.point import Point
from game import constants
from game.laser import Laser
import random

import arcade

class Alien(arcade.Sprite):
    def __init__(self, x, y):
        super().__init__(constants.ALIEN_IMAGE)

        self.center_x = x
        self.center_y = y

        


