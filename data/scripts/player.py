import pygame

class Player(pygame.sprite.Sprite):
    '''
    This Class is the player class which will be controlled by User/Gamer.
    '''
    def __init__(self, img_path, posX, posY, resize):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img_path), resize)
        self.rect = self.image.get_rect()
        self.xChange = 0
        self.yChange = 0
        self.xPos = posX
        self.yPos = posY
        self.rect.topleft = (posX, posY)
        self.player_group = pygame.sprite.Group()
        self.current_sprite = 0

    def collision_tiles(self, tiles, axis):
        '''
        This function returns top, bottom, right, left to True,
        If collided with tiles.
        '''
        # For X axis
        if axis == 'X':
            self.collisionX = {
                'right': False,
                'left': False
            }
            collided = pygame.sprite.spritecollide(self, tiles, False)
            if collided:
                if self.xChange > 0:
                    self.rect.x = collided[0].rect.left - self.rect.width
                    self.collisionX['right'] = True
                if self.xChange < 0:
                    self.rect.x = collided[0].rect.right
                    self.collisionX['left'] = True
            return self.collisionX

        # For Y axis
        if axis == 'Y':
            self.collisionY = {
                'top': False,
                'bottom': False
            }
            collided = pygame.sprite.spritecollide(self, tiles, False)
            if collided:
                if self.yChange > 0:
                    self.rect.y = collided[0].rect.top - self.rect.height
                    self.collisionY['bottom'] = True
                if self.yChange < 0:
                    self.rect.y = collided[0].rect.bottom
                    self.collisionY['top'] = True
            return self.collisionY

    def __repr__(self):
        return f'PlayerImg:{self.image}\nPlayerCoor:{self.rect.x},{self.rect.y}'