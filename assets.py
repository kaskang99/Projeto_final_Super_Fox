import pygame
import os
import config

#---IMAGENS DO JOGO---
img_dir = path.join(path.dirname(__file__), 'img')

fox_jump = 'fox_jump'
fox_still = 'fox_still'
fox_walk_patas_frente = 'fox_walk_patas_frente'
fox_walk_patas_tras = 'fox_walk_patas_tras'
jacare_dir_frente = 'jacare_dir_frente'
jacare_dir_tras = 'jacare_dir_tras'
lion_dir = 'lion_dir'
lion_esq = 'lion_esq'

def load_assets():
    assets = {}
    assets[fox_jump] = pygame.image.load(os.path.join(img_dir, 'fox_jump.png')).convert()
    assets[fox_still] = pygame.image.load(os.path.join(img_dir, 'fox_still.png')).convert()
    assets[fox_walk_patas_frente] = pygame.image.load(os.path.join(img_dir, 'fox_walk_patas_frente.png')).convert()
    assets[fox_walk_patas_tras] = pygame.image.load(os.path.join(img_dir, 'fox_walk_patas_tras.png')).convert()
    assets[jacare_dir_frente] = pygame.image.load(os.path.join(img_dir, 'jacare_dir_frente.png')).convert()
    assets[jacare_dir_tras] = pygame.image.load(os.path.join(img_dir, 'jacare_dir_tras.png')).convert()
    assets[lion_dir] = pygame.image.load(os.path.join(img_dir, 'lion_dir.png')).convert()
    assets[lion_esq] = pygame.image.load(os.path.join(img_dir, 'lion_esq.png')).convert()