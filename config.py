# game config
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = 'SUPER FOX'
FONT = 'arial'
SPRITESHEET = 'spritesheet_jumper.png'
FOX_SPRITE = 'fox_spritesheet.png'
HS_FILE = "highscore.txt"
# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 1
PLAYER_JUMP = 20

#iniciar plataformas
PLATFORM_LIST = [(0, HEIGHT -60), 
                (310, HEIGHT -60), 
                (850, HEIGHT -60),
                (WIDTH/3, HEIGHT*1/2),
                (350, 200)]

# cores
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (100, 240, 255)
LIGHTGREY = (100, 100, 100)
YELLOW = (255, 255, 0)

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
