from game import constants
from game.action import Action
from game.laser import Laser

import random

class ControlActorsAction(Action):
    """A code template for controlling actors. The responsibility of this
    class of objects is translate user input into some kind of intent.
    
    Stereotype:
        Controller

    Attributes:
        _input_service (InputService): An instance of InputService.
    """

    def __init__(self, input_service):
        """The class constructor.
        
        Args:
            input_service (InputService): An instance of InputService.
        """
        self._input_service = input_service
        self.ship_change_x = 0
        self.frames_since_last_move = 0

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """

        self._input_service.shoot_laser(cast)
        
        direction = self._input_service.get_direction().scale(constants.SHIP_MOVE_SCALE)
        
        ship = cast["ship"][0] # there's only one in the cast 

        direction_to_move = 1
        if direction.get_x() < 0:
            direction_to_move = -1

        if self.frames_since_last_move >= 6 and direction.get_x() != 0:
            ship.change_x = constants.ALIEN_WIDTH * 2 * direction_to_move
            
            self.frames_since_last_move = 0
        else:
            ship.change_x = 0
            self.frames_since_last_move += 1

        ship.change_x = direction.get_x() #this line undoes all the code above
        ship.change_y = direction.get_y() 