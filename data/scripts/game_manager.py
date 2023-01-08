__author__ = "Dhyanesh Ghaghada"

# try:
    # Importing Libraries
import sys
import pygame
from pygame.locals import *

# importing local files
from .config import *
from .cursor import Cursor
from .player import Player
from .tilemap import Tilemap
from .gun import Gun

    # print("ALL LIBRARIES IMPORTED SUCCESSFULLY.")
# except:
    # print("ERROR: CANNOT IMPORT ALL LIBRARIES.")
    # sys.exit()

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

# initialising pygame
pygame.init()

# this class will handle the game.
class Game:
    '''
    This Class will handle the stuff when running the game.
    It is the main class where every thing will combine.
    '''
    def __init__(self, FPS):
        # width and height of the game.
        self.width = WIDTH
        self.height = HEIGHT
        # pygame screen
        self.screen = pygame.display.set_mode((self.width, self.height))
        # running variable is to check if game is still running.
        self.running = True
        # function to set fps
        self.clock = pygame.time.Clock()
        # value of fps
        self.fps = FPS
        # delta time
        self.dt = 0
        # Loading all the variables and stuff.
        self.load()

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

    # This will load variables or anything.
    def load(self):
        '''
        This is function is called to load stuff.
        i.e. variables.
        '''

        self.cursor = Cursor(cursor_path, cursor_size)

        self.world = Tilemap(tiles) # Initializing Tilemap.
        self.world.load_tiles(levels[0], TILE_SIZE) # loading tiles.
        
        self.player = Player(player_img, 14*TILE_SIZE[0], 12*TILE_SIZE[1], PLAYER_SIZE) # creating a player.
        self.player.player_group.add(self.player) # Adding player to sprite group.
        
        self.gun = Gun(gun_img_path, gun_size, (self.player.rect.centerx, self.player.rect.centery))

        self.y_vel = 0 # y-axis velocity.
        
        self.jump_force = jump_force
        self.is_jumping = False
        
        self.x_shift = 0 #player_speed
        self.is_shifting = False

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

    def user_input(self):
        '''
        This function is used to handle all the key pressed.
        '''

        keys_pressed = {
            'W':False,
            'S':False,
            'A':False,
            'D':False
        }
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:
            keys_pressed['W'] = True
        if keys[pygame.K_s]:
            keys_pressed['S'] = True
        if keys[pygame.K_a]:
            keys_pressed['A'] = True
        if keys[pygame.K_d]:
            keys_pressed['D'] = True

        return keys_pressed

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
    
    def calculations(self):
        '''
        All the calculations which are to be done in every frame are written here.
        '''

        self.dt = self.clock.tick(self.fps)/1000 # '/1000' to get the real and more precise value.

        self.cursor.update_pos()

        self.keys_pressed = self.user_input()
        
        self.player.xChange = 0
        self.player.yChange = 0

        # Keys Movements
        if self.is_jumping != True:
            if self.keys_pressed['W']:
                self.is_jumping = True

        if self.keys_pressed['S']:
            pass

        if self.keys_pressed['A'] and self.is_shifting != True:
            self.player.xChange -= player_speed
            
        if self.keys_pressed['D'] and self.is_shifting != True:
            self.player.xChange += player_speed
        
        self.player.rect.x += self.player.xChange
        
        # For Collision in X coordinate
        self.collisionX = self.player.collision_tiles(self.world.tile_group, 'X')
        if self.collisionX['right']:
            pass
        if self.collisionX['left']:
            pass

        # Creating Gravity for the player.
        self.y_vel += G
        self.player.yChange += self.y_vel

        # this occurs true when w key is pressed.
        if self.is_jumping:
            self.player.yChange += self.jump_force

        self.player.rect.y += self.player.yChange * self.dt
        
        # For Collision in Y coordinate
        self.collisionY = self.player.collision_tiles(self.world.tile_group, 'Y')
        """
        if player collides in bottom with tiles then setting value to 0.
        Or it will increase continuously.
        """
        if self.collisionY['bottom']:
            self.y_vel = 0
            self.is_jumping = False
        if self.collisionY['top']:
            self.is_jumping = False

        # self.gun.rotate(1, self.player)

        # Setting player's pos = gun's pos.
        self.gun.rect.x = self.player.rect.centerx
        self.gun.rect.y = self.player.rect.centery

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

    def rendering(self):
        '''
        Stuff related to drawing is been done here.
        '''
        self.player.player_group.draw(self.screen)
        self.world.draw_tiles(self.screen, self.x_shift)
        self.gun.draw(self.screen)
        self.cursor.draw(self.screen)

        # Animation Code.
        if self.is_jumping != True:
            if self.player.xChange == 0:
                Funcs.animate(self.player, player_img_idle, player_anime_speed_idle*self.dt)
            elif self.player.xChange > 0:
                Funcs.animate(self.player, player_img_run_right, player_anime_speed_run*self.dt)
            elif self.player.xChange < 0:
                Funcs.animate(self.player, player_img_run_left, player_anime_speed_run*self.dt)
        else:
            if self.player.xChange > 0:
                Funcs.animate(self.player, player_img_jump_right, player_anime_speed_jump*self.dt)
            elif self.player.xChange < 0:
                Funcs.animate(self.player, player_img_jump_left, player_anime_speed_jump*self.dt)

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

    # this function will through every frame.
    def update(self):
        '''
        This function will go throught every frame.
        '''
        self.calculations()
        self.rendering()

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------

    def run(self):
        '''
        This function will run the game.
        It contains the mainloop of the game.
        '''

        while self.running:
            self.screen.fill(BLACKGROUND_COLOR)
            pygame.display.set_caption(str(round(self.clock.get_fps(), 2)))
            
            self.update()
            
            for event in pygame.event.get():
                '''if clicked the cross button at top-right OR clicked escape key,
                    then exit the program.'''
                if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                    print("QUTTING GAME....")
                    self.running = False
                    sys.exit()
            
            # this function is used to update the screen.
            pygame.display.update()
            pygame.display.flip()

# ---------------------------------------------------------------------------------------------
# ---------------------------------------------------------------------------------------------
