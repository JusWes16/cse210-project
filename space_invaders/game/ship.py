from game.point import Point
from game import constants

import arcade

class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.SHIP_IMAGE)

        self._lives = 3
        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.SHIP_Y)