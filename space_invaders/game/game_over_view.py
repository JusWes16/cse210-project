import arcade
from game import constants
import game.main_view
from game.highscore import Highscore

class GameOverView(arcade.View):
    def __init__(self, score, music_2):
        super().__init__()
        self.texture= arcade.load_texture(constants.SPACE_IMAGE)
        arcade.set_viewport(0, constants.SCREEN_WIDTH - 1, 0, constants.SCREEN_HEIGHT - 1)
        self._score = score.get_points()
        game_over = arcade.load_sound(constants.GAME_OVER)
        arcade.play_sound(game_over)
        self.music_2 = music_2
    
    def on_draw(self):
        arcade.start_render()
        self.texture.draw_sized(constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2, constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT)
        arcade.draw_text("GAME OVER", constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 + 50, arcade.color.RED, font_size=50, anchor_x='center')
        arcade.draw_text(f'Score: {self._score}', constants.SCREEN_WIDTH / 2, constants.SCREEN_HEIGHT / 2 - 20, arcade.color.GREEN, font_size=50, anchor_x='center')
        Highscore().display_points()
        arcade.draw_text('Back', 50, 10, arcade.color.WHITE, font_size=30, anchor_x='center')
        
    def on_mouse_press(self, _x, _y, _button, _modifiers):
        if _x in range(10, 90) and _y in range(10, 50):
            view = game.main_view.MainView(True)
            self.window.show_view(view)
