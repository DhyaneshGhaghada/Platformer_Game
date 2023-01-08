import pygame
from data.scripts.game_manager import Game

FPS = 60
game = Game(FPS)

if __name__ == '__main__':
	game.run()