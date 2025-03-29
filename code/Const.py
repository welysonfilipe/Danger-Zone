import pygame as pg

# C
C_YELLOW = (255, 223, 0)
C_WHITE = (255, 255, 255)
C_ORANGE = (255, 165, 79)
C_BLACK = (000, 000, 000)

# E
ENTITY_SPEED = {
    'Level1Bg0': 0,
    'Level1Bg1': 1,
    'Level1Bg2': 2,
    'Level1Bg3': 2,
    'Level1Bg4': 3,
    'Level1Bg5': 4,
    'Level1Bg6': 5,
    'Level1Bg7': 6,
    'Level1Bg8': 6,
    'Player': 3,
    'PlayerShot': 3,
    'Enemy1': 2,
    'Enemy1Shot': 5,
    'Enemy2': 2,
    'Enemy2Shot': 3

}

EVENT_ENEMY = pg.USEREVENT + 1

ENTITY_HEALTH = {
    'Level1Bg0': 999,
    'Level1Bg1': 999,
    'Level1Bg2': 999,
    'Level1Bg3': 999,
    'Level1Bg4': 999,
    'Level1Bg5': 999,
    'Level1Bg6': 999,
    'Level1Bg7': 999,
    'Level1Bg8': 999,
    'Player': 400,
    'PlayerShot': 1,
    'Enemy1': 40,
    'Enemy1Shot': 1,
    'Enemy2': 50,
    'Enemy2Shot': 1
}

ENTITY_SHOOT_DELAY = {
    'Player': 5,
    'Enemy1': 100,
    'Enemy2': 100
}

ENTITY_DAMAGE = {
    'Level1Bg0': 0,
    'Level1Bg1': 0,
    'Level1Bg2': 0,
    'Level1Bg3': 0,
    'Level1Bg4': 0,
    'Level1Bg5': 0,
    'Level1Bg6': 0,
    'Level1Bg7': 0,
    'Level1Bg8': 0,
    'Player': 1,
    'PlayerShot': 25,
    'Enemy1': 1,
    'Enemy1Shot': 20,
    'Enemy2': 1,
    'Enemy2Shot': 15
}

# M
MENU_OPTION = ('NEW GAME',
               'SCORE',
               'EXIT')

# P
PLAYER_KEY_SHOOT = {'Player': pg.K_SPACE}

# S
SPAWN_TIME = 4000

# W
WIN_WIDTH = 640
WIN_HEIGHT = 360
