from game.laser import Laser
import sys
from game.point import Point
from game import constants

import arcade

class ArcadeInputService:
    """Detects player input. The responsibility of the class of objects is to detect and communicate player keypresses.

    Stereotype: 
        Service Provider

    Attributes:
        _keys (list): up, dn, lt, rt.
    """

    def __init__(self):
        """The class constructor."""
        self._keys = []
        self.laser_shoot = arcade.load_sound(constants.LASER_SHOOT)
        self.can_shoot = True
    
    def set_key(self, key, modifiers):
        #Ignoring modifies at this point...
        self._keys.append(key)

    def remove_key(self, key, modifiers):
        self._keys.remove(key)

    def get_direction(self):
        """Gets the selected direction for the given player.

        Returns:
            Point: The selected direction.
        """
        x = 0
        y = 0

        if arcade.key.LEFT in self._keys or arcade.key.A in self._keys:
            x = -1
        elif arcade.key.RIGHT in self._keys or arcade.key.D in self._keys:
            x = 1
        if arcade.key.UP in self._keys or arcade.key.W in self._keys:
            y = 1
        elif arcade.key.DOWN in self._keys or arcade.key.S in self._keys:
            y = -1

        self.will_shoot()
        
        velocity = Point(x, y)
        return velocity

    def will_shoot(self):
        if arcade.key.SPACE not in self._keys:
            self.can_shoot = True
    
    def shoot_laser(self, cast):
        ship = cast["ship"][0]
        if arcade.key.SPACE in self._keys:
            if self.can_shoot:
                x = ship.center_x
                y = ship.center_y
                laser = Laser(x, y)
                cast["lasers"].append(laser) 
                arcade.play_sound(self.laser_shoot)
                self.can_shoot = False

        else:
            pass