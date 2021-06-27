from game.action import Action
from game import constants

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()

        aliens = cast["aliens"]

        for alien in aliens:
            self._output_service.draw_actor(alien)

        for laser in cast["lasers"]:
            self._output_service.draw_actor(laser)

        ship = cast["ship"][0] # there's only one
        self._output_service.draw_actor(ship)

        self._output_service.flush_buffer()


