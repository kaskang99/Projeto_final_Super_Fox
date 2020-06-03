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
                (250, HEIGHT -60), 
                (500, HEIGHT -60),
                (925, HEIGHT -60),
                (1300, HEIGHT -60),
                (1500, HEIGHT -60),
                (1925, HEIGHT -60),
                (2225, HEIGHT -240),
                (2700, HEIGHT -60),
                (2900, HEIGHT -60),
                (3300, HEIGHT -60),
                (3650, HEIGHT -240),
                (4000, HEIGHT -410),]

# cores
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
TEAL = (0, 128, 128)
SKYBLUE = (135, 206, 235)
LIGHTGREY = (100, 100, 100)
YELLOW = (255, 255, 0)
PLAYER_GREEN = (0, 51.8, 0)

TILESIZE = 32
GRIDWIDTH = WIDTH / TILESIZE
GRIDHEIGHT = HEIGHT / TILESIZE
