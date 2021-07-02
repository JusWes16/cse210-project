from game.point import Point
from game import constants

import arcade

class Score():
    def __init__(self):
        self._score = 200
        self.change_y = 0
        self.change_x = 0
        self.center_x = constants.SCORE_X
        self.center_y = constants.SCORE_Y

    def draw(self):
        # self._score = score

        output = f"Score: {self._score}"
        arcade.draw_text(output, self.center_x, self.center_y, arcade.color.GREEN, 18)