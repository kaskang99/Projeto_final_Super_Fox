import pygame
from config import *
from assets import *
from sprites import *


#---tela do jogo---
def game_screen(window):
    clock = pygame.time.Clock()

    assets = load_assets()

