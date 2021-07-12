import random
from game.point import Point
import arcade
from game import constants

class Highscore(arcade.Sprite):
    """Points earned. The responsibility of Score is to keep track of the player's points.

    Stereotype:
        Information Holder

    Attributes: 
        _points (integer): The number of points the food is worth.
    """
    def __init__(self):
        """The class constructor. Invokes the superclass constructor, initializes 
        points to zero, sets the position and updates the text.
        
        Args:
            self (Score): an instance of Score.
        """
        super().__init__()
        with open(constants.HS_FILE, 'r') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        self._text = (f"Highscore: {self.highscore}")
    
    def new_highscore(self, points):
        """Adds the given points to the running total and updates the text.
        
        Args:
            self (Score): An instance of Score.
            points (integer): The points to add.
        """
        if points > self.highscore:
            self.highscore = int(points)
            with open(constants.HS_FILE, 'w') as f:
                f.write(str(self.highscore))

        self._text = (f"Score: {self.highscore}")
    
    def get_highscore(self):
        return self.highscore
    
    def display_points(self):
        arcade.draw_text(f'{self._text}', constants.SCREEN_WIDTH / 2 - 150, constants.SCREEN_HEIGHT / 2 - 80, arcade.color.GREEN, font_size=45)