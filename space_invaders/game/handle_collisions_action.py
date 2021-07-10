import random
from game.action import Action
from game import constants
from game.smoke import Smoke
from game.particle import Particle
import arcade

class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """
    def __init__(self, score, explosions, output_service):
        self._score = score
        self.explosions_list = explosions
        self._output_service = output_service
        
    def execute(self, cast):
        """Executes the action using the given actors.

        Args:
            cast (dict): The game actors {key: tag, value: list}.
        """
        lasers = cast['lasers']
        ship = cast['ship'][0]

        self._handle_walls_collision(ship)

        for laser in cast["lasers"]:
            aliens = cast["aliens"]
            self._handle_laser_collision(lasers, laser, aliens, ship)
    
    def _handle_walls_collision(self, ship):
        if ship.center_x < 20:
            ship.center_x = 20
        elif ship.center_x > 780:
            ship.center_x = 780
        
        if ship.center_y < 65:
            ship.center_y = 65
        elif ship.center_y > 200:
            ship.center_y = 200
        

    def _handle_laser_collision(self, lasers, laser, aliens, ship):
        laser_to_remove = None
        alien_to_remove = None
        invader_killed = arcade.load_sound(constants.INVADER_KILLED)

        for alien in aliens:
            if laser.collides_with_sprite(alien) and laser.change_y > 0:
                laser_to_remove = laser
                alien_to_remove = alien
                self._score.add_points(5)
                arcade.play_sound(invader_killed)
        
        if laser.collides_with_sprite(ship) and laser.change_y < 0:
            ship._lives -= 1
            laser_to_remove = laser
            smoke = Smoke(50)
            smoke.position = ship.position
            self.explosions_list.append(smoke)
            for i in range(constants.PARTICLE_COUNT):
                    particle = Particle(self.explosions_list)
                    particle.position = ship.position
                    self.explosions_list.append(particle)
            ship.center_x = int(constants.MAX_X / 2)
            ship.center_y = int(constants.SHIP_Y)
            

        if laser.center_y < 45 or laser.center_y > constants.MAX_Y:
            laser_to_remove = laser
        
        if alien_to_remove != None:
            aliens.remove(alien_to_remove)
            
        if laser_to_remove != None:
            lasers.remove(laser_to_remove)
    

    def _is_off_screen(self, laser):
        return laser.center_y < 0