# Sprite classes for game
from config import *
import pygame as pg
vec = pg.math.Vector2

class Player(pg.sprite.Sprite):
    def __init__(self, game): #no arquivo MAIN.py - self.player = Player(self) - o init precisa de mais de 1 argumento, já que não é mais Player() e sim Player(self)
        pg.sprite.Sprite.__init__(self)
        self.game = game #Agora a classe Player tem como referência o jogo.
        self.image = pg.Surface((TILESIZE, TILESIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, 600)
        self.pos = vec(WIDTH/5, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def jump(self):
        #pular somente se estiver em uma plataforma ou estiver no chao
        self.rect.x += 1 #adicionei um pixel para o retângulo do jogador (verificar se tem ou não uma plataforma)
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1 #retirei o pixel de verificação
        if hits:
            self.vel.y = -PLAYER_JUMP

    def update(self):
        self.acc = vec(0,PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT]:
            self.acc.x = -PLAYER_ACC
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        
        # implementacao do atrito
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #eq of motion
        self.vel += self.acc
        self.pos += self.vel + 0.5*self.acc
        # jogador sai pra fora da tela e volta do outro lado
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self. rect.midbottom = self.pos

class Platform(pg.sprite.Sprite):
    def __init__(self, x, y, w, h):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((w,h))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

