import arcade
from game import constants
import game.instructions_view
from game.invaders import Invaders
from game.highscore import Highscore

class MainView(arcade.View):
    def on_show(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH -1, 0, constants.SCREEN_HEIGHT -1)
        self.texture= arcade.load_texture(constants.SPACE_IMAGE)
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("SPACE INVADERS", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 70, arcade.color.GREEN, font_size=40, anchor_x='center')
        arcade.draw_text("Play", 70, constants.SCREEN_HEIGHT / 2, arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text("How to Play", 168, constants.SCREEN_HEIGHT / 2 - 85, arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text(f"High Score: {Highscore().get_highscore()}", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 110, arcade.color.RED, font_size=30, anchor_x='center')
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(12, 128) and _y in range(303, 363):
            view = Invaders()
            view.setup()
            self.window.show_view(view)

        if _x in range(12, 325) and _y in range(218, 274):
            view = game.instructions_view.InstructionsView()
            self.window.show_view(view)
    
    