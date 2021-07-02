from game import constants
from game.main_view import MainView
import arcade

def main():
    # start the game
    window = arcade.Window(constants.SCREEN_WIDTH, constants.SCREEN_HEIGHT, constants.SCREEN_TITLE)
    start_view = MainView()
    window.show_view(start_view)
    arcade.run()

if __name__ == "__main__":
    main()