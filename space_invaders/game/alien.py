from game.point import Point
from game import constants
from game.laser import Laser
import random

import arcade

class Alien(arcade.Sprite):
    def __init__(self, x, y):
        num = random.randint(1, 4)
        if num == 1:
            super().__init__(constants.ALIEN_IMAGE1)
        if num == 2:
            super().__init__(constants.ALIEN_IMAGE2)
        if num == 3:
            super().__init__(constants.ALIEN_IMAGE3)
        if num == 4:
            super().__init__(constants.ALIEN_IMAGE4)

        self.center_x = x
        self.center_y = y

        


