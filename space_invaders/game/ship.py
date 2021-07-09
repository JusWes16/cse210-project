from game.point import Point
from game import constants

import arcade

class Ship(arcade.Sprite):
    def __init__(self):
        super().__init__(constants.SHIP_IMAGE)

        self.center_x = int(constants.MAX_X / 2)
        self.center_y = int(constants.SHIP_Y)

        self._lives = 3

    def remove_life(self):
        self._lives -= 1
        if self._lives == 0:
            super().__init__(constants.ALIEN_IMAGE1)