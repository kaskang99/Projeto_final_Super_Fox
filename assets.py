import pygame
from os import *
import os
from config import *

#---IMAGENS DO JOGO---
img_dir = path.join(path.dirname(__file__), 'assets','img')

fox_jump = 'fox_jump'
fox_still = 'fox_still'
fox_walk_patas_frente = 'fox_walk_patas_frente'
fox_walk_patas_tras = 'fox_walk_patas_tras'
jacare_dir_frente = 'jacare_dir_frente'
jacare_dir_tras = 'jacare_dir_tras'
lion_dir = 'lion_dir'
lion_esq = 'lion_esq'
background = 'background'
flag = 'flag'

def load_assets():
    assets = {}
    assets[background] = pygame.image.load(os.path.join(img_dir, 'background.png')).convert()
    assets[flag] = pygame.image.load(os.path.join(img_dir, 'flagRed.png')).convert()
    return assets