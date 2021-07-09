from game.action import Action
from game import constants
from game.score import Score

import arcade

class DrawActorsAction(Action):
    """A code template for drawing actors.
    
    Stereotype:
        Controller

    Attributes:
        _output_service (OutputService): An instance of OutputService.
    """

    def __init__(self, output_service, score, texture):
        """The class constructor.
        
        Args:
            _output_service (OutputService): An instance of OutputService.
        """
        self._output_service = output_service
        self._score = score
        self.texture = texture

    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        self._output_service.clear_screen()

        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)

        aliens = cast["aliens"]

        arcade.draw_line(10, 40, 790, 40, arcade.color.WHITE)
        self._score.display_points()
        arcade.draw_text('Lives:', 630, 7, arcade.color.GREEN, font_size=20)

        for alien in aliens:
            self._output_service.draw_actor(alien)

        for laser in cast["lasers"]:
            self._output_service.draw_actor(laser)

        ship = cast["ship"][0] # there's only one
        self._output_service.draw_actor(ship)

        self._output_service.flush_buffer()


