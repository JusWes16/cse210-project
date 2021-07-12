from game import constants
from game.main_view import MainView
import arcade

def main():
    # start the game
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    music = arcade.load_sound(constants.MUSIC)
    music_2 = arcade.play_sound(music)
    start_view = MainView(False, music_2)
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()