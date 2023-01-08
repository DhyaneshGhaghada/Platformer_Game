# importing libraries
import pygame
import os

from .functions import Funcs

window_size = 1

# size of the window
WIDTH = 1200/window_size
HEIGHT = 700/window_size
# frames per second
FPS = 150

# all the RGB colors
colors = {
    'BLACK':(0, 0, 0),
    'DIM_GRAY':(105, 105, 105),
    'WHITE':(255, 255, 255),
    'CYAN':(0, 255, 255)
}

BLACKGROUND_COLOR = colors['CYAN']

# Gravity
Gvel = 0
G = 9.8 # Evaluation: 0.392


player_anime_speed_idle = 8
player_anime_speed_run = 12
player_anime_speed_jump = 1

PLAYER_SIZE = (11*2.5, 16*2.5)

player_img_idle = Funcs.folder_to_img('data/sprites/player/player_idle', PLAYER_SIZE)
player_img_run_right = Funcs.folder_to_img('data/sprites/player/player_run', PLAYER_SIZE)
player_img_run_left = [ pygame.transform.flip(img, True, False) for img in player_img_run_right ]
player_img_jump_right = Funcs.folder_to_img('data/sprites/player/player_jump', PLAYER_SIZE)
player_img_jump_left = [ pygame.transform.flip(img, True, False) for img in player_img_jump_right ]

player_img = 'data/sprites/player/player_idle/1.png'

player_speed = 10
jump_force = -500

tiles = {
    '1':'data/sprites/tiles/4Palette_tiles/1.png',
    '2':'data/sprites/tiles/4Palette_tiles/2.png',
    '3':'data/sprites/tiles/4Palette_tiles/3.png',
    '4':'data/sprites/tiles/4Palette_tiles/4.png',
    '5':'data/sprites/tiles/4Palette_tiles/5.png',
    '6':'data/sprites/tiles/4Palette_tiles/6.png',
    '7':'data/sprites/tiles/4Palette_tiles/7.png',
    '8':'data/sprites/tiles/4Palette_tiles/8.png',
    '9':'data/sprites/tiles/4Palette_tiles/9.png',
    '10':'data/sprites/tiles/4Palette_tiles/10.png',
    '11':'data/sprites/tiles/4Palette_tiles/11.png'
}

TILE_SIZE = (40/window_size,40/window_size)

levels = [
    'data/levels/level1'
]

gun_img_path = 'data/sprites/weapons/shotgun.png'
gun_size = (13*2.5, 4*2.5)

cursor_path = 'data/sprites/cursor/cursor_idle.png'
cursor_size = (10*2, 12*2)