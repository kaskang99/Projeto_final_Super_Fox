# game config
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = 'SUPER FOX'
FONT = 'arial'
SPRITESHEET = 'spritesheet_jumper.png'
FOX_SPRITESHEET = 'fox_spritesheet.png'
# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 1
PLAYER_JUMP = 20

#iniciar plataformas
PLATFORM_LIST = [(0, HEIGHT -40, WIDTH, 40), 
                (WIDTH/2 - 50, HEIGHT * 3/4 - 50, 100, 20), 
                (125, HEIGHT-350, 100, 20),
                (WIDTH/3, HEIGHT*1/2, 100, 20),
                (350, 200, 50, 20)]

# cores
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
SPRITE_BG = (0, 50.2, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 129)
LIGHTGREY = (100, 100, 100)

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
