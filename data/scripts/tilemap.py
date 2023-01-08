import pygame
from .tile import Tile

class Tilemap(pygame.sprite.Sprite):
    def __init__(self, tiles):
        self.tiles = tiles
        self.tile_group = pygame.sprite.Group()

    def __repr__(self):
        return f'Tiles: {self.tiles}\nTile_Group: {self.tile_group}'

    # This function loads tiles.
    def load_tiles(self, map_file, tile_size, is_bg=False):
        '''
        Takes lvl file and loads tiles. note it does not draw, it only loads.
        '''
        ext = '.lvl'
        if is_bg:
            ext = '.bgmap'
        
        with open(f'{map_file}{ext}', 'r') as file:
            data = file.read()
            map_data = []
            for i in data.split('\n'):
                temp_list=[]
                '''
                this temp list is used to store each word/letter in level file which is appended to map_data after.
                later we again reset the list to empty.
                '''
                for j in i.split(' '):
                    temp_list.append(j)
                map_data.append(temp_list)
            file.close()
        
        row = 0
        for i in map_data:
            col = 0
            for tile in i:
                for num in self.tiles.keys():
                    if tile == num:
                        pos = (col*tile_size[0], row*tile_size[1])
                        tile_obj = Tile(self.tiles[num], tile_size)
                        tile_obj.rect.x = pos[0]
                        tile_obj.rect.y = pos[1]
                        self.tile_group.add(tile_obj)
                col += 1
            row += 1

    def draw_tiles(self, screen, x_shift):
        self.tile_group.update(x_shift)
        self.tile_group.draw(screen)