import pygame

class Cursor(pygame.sprite.Sprite):
    
    def __init__(self, img_path, resize):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load(img_path), resize)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pygame.mouse.get_pos()
        self.cursor_group = pygame.sprite.Group()
        self.cursor_group.add(self)
        pygame.mouse.set_visible(False)

    def update_pos(self):
        self.rect.x, self.rect.y = pygame.mouse.get_pos()
    
    def draw(self, screen):
        self.cursor_group.draw(screen)