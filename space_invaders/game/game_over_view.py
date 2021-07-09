import arcade
from game import constants
import game.main_view

class GameOverView(arcade.View):
    def __init__(self):
        super().__init__()
        self.texture= arcade.load_texture(constants.GAME_OVER_IMAGE)

        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        game_view = game.main_view.MainView()
        game_view.setup()
        self.window.show_view(game_view)
