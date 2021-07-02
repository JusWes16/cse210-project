import arcade
from game import constants
import game.instructions_view
from game.invaders import Invaders

class MainView(arcade.View):
    def on_show(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH -1, 0, constants.SCREEN_HEIGHT -1)
    
    def on_draw(self):
        arcade.start_render()
        arcade.draw_text("Play", 70, constants.SCREEN_HEIGHT / 2, arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text("How to Play", 168, constants.SCREEN_HEIGHT / 2 - 85, arcade.color.WHITE, font_size=50, anchor_x='center')
        # arcade.draw_rectangle_outline(70, 333, 115, 60, arcade.color.WHITE)
        # arcade.draw_rectangle_outline(170, 246, 310, 55, arcade.color.WHITE)
    
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(12, 128) and _y in range(303, 363):
            view = Invaders()
            view.setup()
            self.window.show_view(view)

        if _x in range(12, 325) and _y in range(218, 274):
            view = game.instructions_view.InstructionsView()
            self.window.show_view(view)
    
    