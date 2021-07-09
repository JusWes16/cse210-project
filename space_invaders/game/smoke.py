import arcade
from game import constants

class Smoke(arcade.SpriteCircle):
    """ This represents a puff of smoke """
    def __init__(self, size):
        super().__init__(size, arcade.color.LIGHT_GRAY, soft=True)
        self.change_y = constants.SMOKE_RISE_RATE
        self.scale = constants.SMOKE_START_SCALE

    def update(self):
        """ Update this particle """
        if self.alpha <= constants.PARTICLE_FADE_RATE:
            # Remove faded out particles
            self.remove_from_sprite_lists()
        else:
            # Update values
            self.alpha -= constants.SMOKE_FADE_RATE
            self.center_x += self.change_x
            self.center_y += self.change_y
            self.scale += constants.SMOKE_EXPANSION_RATE