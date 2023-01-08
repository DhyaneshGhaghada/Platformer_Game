import pygame

class Tile(pygame.sprite.Sprite):
    '''
    This class will handle all the code related to tiles.
    '''
    def __init__(self, tile_path, tile_size):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(tile_path), tile_size)
        self.rect = self.image.get_rect()
    
    def update(self, x_shift):
        self.rect.x += x_shift
        
    def __repr__(self):
        return f'TILE IMAGE: {self.image}\nTILE RECT: {self.rect}'