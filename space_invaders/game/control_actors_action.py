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

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._input_service.shoot_laser(cast)
        direction = self._input_service.get_direction().scale(constants.SHIP_MOVE_SCALE)
        ship = cast["ship"][0] # there's only one in the cast
        ship.change_x = direction.get_x()
        ship.change_y = direction.get_y()

        for alien in cast["aliens"]:
            if random.randint(0, 80) == 1:
                laser = Laser(alien.center_x, alien.center_y, True)
                cast["lasers"].append(laser)