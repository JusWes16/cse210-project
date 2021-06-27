import random
from game import constants
from game.point import Point
from game.control_actors_action import ControlActorsAction
from game.draw_actors_action import DrawActorsAction
from game.handle_collisions_action import HandleCollisionsAction
from game.move_actors_action import MoveActorsAction
from game.arcade_input_service import ArcadeInputService
from game.arcade_output_service import ArcadeOutputService

from game.ship import Ship
from game.alien import Alien
from game.laser import Laser

from game.invaders import Invaders
import arcade

def main():

    # create the cast {key: tag, value: list}
    cast = {}

    ship = Ship()
    cast["ship"] = [ship]

    cast["lasers"] = []
    
    cast["aliens"] = []
    for x in range(constants.ALIEN_WIDTH * 2,
                constants.MAX_X - constants.ALIEN_WIDTH * 2,
                constants.ALIEN_WIDTH + constants.ALIEN_SPACE):
        for y in range(int(constants.MAX_Y * .7),
                    int(constants.MAX_Y * .9),
                    constants.ALIEN_HEIGHT + constants.ALIEN_SPACE):
            alien = Alien(x, y)
            cast["aliens"].append(alien)



    # create the script {key: tag, value: list}
    script = {}

    input_service = ArcadeInputService()
    output_service = ArcadeOutputService()
    
    control_actors_action = ControlActorsAction(input_service)
    move_actors_action = MoveActorsAction()
    handle_collisions_action = HandleCollisionsAction()
    draw_actors_action = DrawActorsAction(output_service)
    
    script["input"] = [control_actors_action]
    script["update"] = [move_actors_action, handle_collisions_action]
    script["output"] = [draw_actors_action]

    # start the game
    invaders = Invaders(cast, script, input_service)
    invaders.setup()
    arcade.run()


if __name__ == "__main__":
    main()