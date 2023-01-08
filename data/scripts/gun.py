import pygame

class Gun(pygame.sprite.Sprite):
    
    def __init__(self, img_path, resize, pos):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img_path), resize)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos[0], pos[1]
        self.gun_group = pygame.sprite.Group()
        self.gun_group.add(self)
        self.angle = 0
    
    def rotate(self, angle, player):
        '''
        Rotate gun based on the cursor's position.
        '''
        self.angle += angle
        self.image = pygame.transform.rotate(self.image, self.angle)
        self.rect.x, self.rect.y = player.rect.x, player.rect.y

    def draw(self, screen):
        self.gun_group.draw(screen)