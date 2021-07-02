import os

MAX_X = 800
MAX_Y = 600

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = 'Space Invaders'

LASER_SPEED = 12
ALIEN_LASER_SPEED = -8
LASER_Y = MAX_Y / 2

SHIP_Y = 25

SHIP_MOVE_SCALE = 10

ALIEN_WIDTH = 25
ALIEN_HEIGHT = 15
ALIEN_SPACE = 10

PATH = os.path.dirname(os.path.abspath(__file__))

LASER_IMAGE = os.path.join(PATH, '..', 'assets', 'images', 'laser.png')
ALIEN_LASER_IMAGE = os.path.join(PATH, '..', 'assets', 'images', 'alien_laser.png')
SHIP_IMAGE = os.path.join(PATH, '..', 'assets', 'images', 'spaceship.png')
ALIEN_IMAGE = os.path.join(PATH, '..', 'assets', 'images', 'alien.png')

