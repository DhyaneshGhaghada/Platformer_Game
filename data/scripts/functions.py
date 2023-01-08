import pygame
import os

class Funcs:
	'''
	This class contains all the necessary functions.
	'''
	def folder_to_img(path, resize):
		'''
		This Function takes path and returns list of pygame img.
		PARAMETER: path, resize
		RETURNS: LIST of Pygame Img
		'''
		imgs = []
		for i in os.listdir(path):
			img = pygame.transform.scale(pygame.image.load(f'{path}/{i}'), resize)
			imgs.append(img)
		return imgs

	def animate(obj, imgs, anime_speed):
		obj.current_sprite += anime_speed
		if obj.current_sprite >= len(imgs):
			obj.current_sprite = 0
		obj.image = imgs[int(obj.current_sprite)]