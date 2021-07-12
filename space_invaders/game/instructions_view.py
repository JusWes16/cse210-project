import arcade
import game.main_view
from game import constants

class InstructionsView(arcade.View):
    def __init__(self, music_2):
        super().__init__()
        self.music_2 = music_2

    def on_show(self):
        arcade.set_viewport(0, constants.SCREEN_WIDTH -1, 0, constants.SCREEN_HEIGHT -1)
        self.texture= arcade.load_texture(constants.SPACE_IMAGE)
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("How to Play", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT - 75, arcade.color.WHITE, font_size=50, anchor_x='center')
        arcade.draw_text("Use WASD or the arrow keys to move around the spaceship. Avoid \n\ngetting hit by alien lasers, while also shooting the aliens with spacebar.\n\nAfter destroying all aliens, the difficulty will increase. If you are hit by \n\na laser, you lose a life. After all lives are gone, it is game over.", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 75, arcade.color.WHITE, font_size=20, anchor_x='center')
        arcade.draw_text('Back', 50, 10, arcade.color.WHITE, font_size=30, anchor_x='center')
        # arcade.draw_rectangle_outline(50, 30, 80, 40, arcade.color.WHITE)

    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(10, 90) and _y in range(10, 50):
            view = game.main_view.MainView(False, self.music_2)
            self.window.show_view(view)
    