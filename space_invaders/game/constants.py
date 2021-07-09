import os
import arcade

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

SCORE_X = 10
SCORE_Y = 10

ALIEN_WIDTH = 25
ALIEN_HEIGHT = 15
ALIEN_SPACE = 10

PATH = os.path.dirname(os.path.abspath(__file__))

LASER_IMAGE = os.path.join(PATH, '..', 'assets', 'images', 'laser.png')
ALIEN_LASER_IMAGE = os.path.join(PATH, '..', 'assets', 'images', 'alien_laser.png')
SHIP_IMAGE = os.path.join(PATH, '..', 'assets', 'images', 'spaceship.png')
ALIEN_IMAGE1 = os.path.join(PATH, '..', 'assets', 'images', 'alien.png')
ALIEN_IMAGE2 = os.path.join(PATH, '..', 'assets', 'images', 'alien.png')
ALIEN_IMAGE3 = os.path.join(PATH, '..', 'assets', 'images', 'alien3.png')
ALIEN_IMAGE4 = os.path.join(PATH, '..', 'assets', 'images', 'alien4.png')
GAME_OVER_IMAGE = os.path.join(PATH, '..', 'assets', 'images', 'game_over.png')
SPACE_IMAGE = os.path.join(PATH, '..', 'assets', 'images', 'space.png')
SPACE_IMAGE2 = os.path.join(PATH, '..', 'assets', 'images', 'space2.png')
INVADER_KILLED = os.path.join(PATH, '..', 'assets', 'sounds', 'invaderkilled.wav')
LASER_SHOOT = os.path.join(PATH, '..', 'assets', 'sounds', 'shoot.wav')
MUSIC = os.path.join(PATH, '..', 'assets', 'sounds', 'spaceinvaders1.mpeg')

PARTICLE_GRAVITY = 0.05
PARTICLE_FADE_RATE = 8

PARTICLE_MIN_SPEED = 2.5
PARTICLE_SPEED_RANGE = 2.5

PARTICLE_COUNT = 20

PARTICLE_RADIUS = 3

PARTICLE_COLORS = [arcade.color.ALIZARIN_CRIMSON,
                   arcade.color.COQUELICOT,
                   arcade.color.LAVA,
                   arcade.color.KU_CRIMSON,
                   arcade.color.DARK_TANGERINE]


PARTICLE_SPARKLE_CHANCE = 0.02

SMOKE_START_SCALE = 0.25
SMOKE_EXPANSION_RATE = 0.03

SMOKE_FADE_RATE = 7
SMOKE_RISE_RATE = 0.5

SMOKE_CHANCE = 0.25