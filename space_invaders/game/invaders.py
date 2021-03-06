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
from game.highscore import Highscore

from game.ship import Ship
from game.alien import Alien
from game.laser import Laser

import arcade

class Invaders(arcade.View):
    def __init__(self, music_2):
        super().__init__()

        self.texture= arcade.load_texture(constants.SPACE_IMAGE2)
        self.ship_img = arcade.load_texture(constants.SHIP_IMAGE)
        self.explosions_list = None
        self.music_2 = music_2
    
    def create_aliens(self, difficulty):
            for i in range(constants.ALIEN_WIDTH * 2,
                    constants.MAX_X - constants.ALIEN_WIDTH,
                    constants.ALIEN_WIDTH + constants.ALIEN_SPACE):
                for j in range(difficulty):
                    y = constants.MAX_Y - (j + 1) * (constants.ALIEN_HEIGHT + constants.ALIEN_SPACE) 
                    alien = Alien(i, y)
                    self._cast["aliens"].append(alien)
        
    def setup(self):
        self.explosions_list = arcade.SpriteList()

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
        handle_collisions_action = HandleCollisionsAction(self._score, self.explosions_list, self._output_service)
        draw_actors_action = DrawActorsAction(self._output_service, self._score, self.texture, self.explosions_list)
        
        self._script["input"] = [control_actors_action]
        self._script["update"] = [move_actors_action, handle_collisions_action]
        self._script["output"] = [draw_actors_action]
    
    def on_update(self, delta_time):
        self.explosions_list.update()
        self._cue_action("update")
        ship = self._cast['ship'][0]
        if len(self._cast["aliens"]) == 0:
            self.difficulty += 1
            self.create_aliens(self.difficulty)
            ship.center_x = int(constants.MAX_X / 2)
            ship.center_y = int(constants.SHIP_Y)
        if ship._lives == 0:
            Highscore().new_highscore(self._score.get_points())
            view = GameOverView(self._score, self.music_2)
            self.window.show_view(view)

    def on_draw(self):
        arcade.start_render()
        self._cue_action("output")
        ship = self._cast["ship"][0]
        if ship._lives == 3:
            self.ship_img.draw_sized(700, 20, 20, 30)
            self.ship_img.draw_sized(730, 20, 20, 30)
            self.ship_img.draw_sized(760, 20, 20, 30)
        elif ship._lives == 2:
            self.ship_img.draw_sized(700, 20, 20, 30)
            self.ship_img.draw_sized(730, 20, 20, 30)
        elif ship._lives == 1:
            self.ship_img.draw_sized(700, 20, 20, 30)
    
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
