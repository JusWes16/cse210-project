import random
from game.action import Action
from game.score import Score


class HandleCollisionsAction(Action):
    """A code template for handling collisions. The responsibility of this class of objects is to update the game state when actors collide.
    
    Stereotype:
        Controller
    """

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
            self._handle_enemy_laser_collision(lasers, laser, ship)
            self._handle_alien_collision(lasers, laser, aliens)
    
    def _handle_walls_collision(self, ship):
        if ship.center_x < 20:
            ship.center_x = 20
        elif ship.center_x > 780:
            ship.center_x = 780
        
        if ship.center_y < 20:
            ship.center_y = 20
        elif ship.center_y > 200:
            ship.center_y = 200
        
    def _handle_enemy_laser_collision(self, lasers, laser, ship):
        laser_to_remove = None
        
        # score = 0

        
        if laser.collides_with_sprite(ship) and laser.change_y < 0:
            laser_to_remove = laser
            ship.remove_life()
            # score += 50
            # Score().get_score(score)
        
        if laser_to_remove != None:
            lasers.remove(laser_to_remove)

    def _handle_alien_collision(self, lasers, laser, aliens):
        laser_to_remove = None
        alien_to_remove = None
        # score = 0

        for alien in aliens:
            if laser.collides_with_sprite(alien) and laser.change_y > 0:
                laser_to_remove = laser
                alien_to_remove = alien

                # score += 50
                # Score().get_score(score)

        if laser.center_y < 0:
            laser_to_remove = laser
        
        if alien_to_remove != None:
            aliens.remove(alien_to_remove)
        
        if laser_to_remove != None:
            lasers.remove(laser_to_remove)

    def _is_off_screen(self, laser):
        return laser.center_y < 0