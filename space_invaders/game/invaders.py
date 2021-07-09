import random
from game import constants
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService
from game.game_over_view import GameOverView
from game.score import Score

from game.ship import Ship
from game.alien import Alien
from game.laser import Laser

import arcade

class Invaders(arcade.View):
    def __init__(self):
        super().__init__()

        self.texture= arcade.load_texture(constants.SPACE_IMAGE2)
    
    def create_aliens(self, difficulty):
        for i in range(constants.ALIEN_WIDTH * 2,
                    constants.MAX_X - constants.ALIEN_WIDTH * 2,
                    constants.ALIEN_WIDTH + constants.ALIEN_SPACE):
            for j in range(difficulty):
                y = constants.MAX_Y - (j + 1) * (constants.ALIEN_HEIGHT + constants.ALIEN_SPACE) 
                alien = Alien(i, y)
                self._cast["aliens"].append(alien)

                
    def setup(self):
        self._cast = {}

        ship = Ship()
        self._cast["ship"] = [ship]

        self._cast["lasers"] = []
        
        self._score = Score()  
        
        self._cast["aliens"] = []
        
        self.difficulty = 1
        self.create_aliens(self.difficulty)

        # create the script {key: tag, value: list}
        self._script = {}

        self._input_service = ArcadeInputService()
        self._output_service = ArcadeOutputService()
        
        control_actors_action = ControlActorsAction(self._input_service)
        move_actors_action = MoveActorsAction()
        handle_collisions_action = HandleCollisionsAction(self._score)
        draw_actors_action = DrawActorsAction(self._output_service, self._score, self.texture)
        
        self._script["input"] = [control_actors_action]
        self._script["update"] = [move_actors_action, handle_collisions_action]
        self._script["output"] = [draw_actors_action]
    
    def on_update(self, delta_time):
        self._cue_action("update")

        ship = self._cast['ship'][0]
        if ship._lives == 0:
            view = GameOverView()
            self.window.show_view(view)

        if len(self._cast["aliens"]) == 0:
            self.difficulty += 1
            self.create_aliens(self.difficulty)

    def on_draw(self):
        arcade.start_render()
        self._cue_action("output")
    
    def on_key_press(self, symbol, modifiers):
        self._input_service.set_key(symbol, modifiers)
        self._cue_action("input")
    
    def on_key_release(self, symbol, modifiers):
        self._input_service.remove_key(symbol, modifiers)
        self._cue_action("input")

    def _cue_action(self, tag):
        """Executes the actions with the given tag.
        
        Args:
            tag (string): The given tag.
        """ 
        for action in self._script[tag]:
            action.execute(self._cast)