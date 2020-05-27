# game config
WIDTH = 1024
HEIGHT = 768
FPS = 60
TITLE = 'SUPER FOX'
FONT = 'arial'
SPRITESHEET = 'spritesheet_jumper.png'
HS_FILE = "highscore.txt"
# player properties
PLAYER_ACC = 0.5
PLAYER_FRICTION = -0.12
PLAYER_GRAVITY = 1
PLAYER_JUMP = 20

#iniciar plataformas
PLATFORM_LIST = [(0, HEIGHT -40), 
                (WIDTH/2 - 50, HEIGHT * 3/4 - 50), 
                (125, HEIGHT-350),
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
