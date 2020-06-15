# Sprite classes for game
from config import *
import pygame as pg
from os import path
from random import choices
from assets import *
vec = pg.math.Vector2

dir = path.dirname(__file__)
mob_dir = path.join(dir, 'assets')

class Player(pg.sprite.Sprite):
    def __init__(self, game): #no arquivo MAIN.py - self.player = Player(self) - o init precisa de mais de 1 argumento, já que não é mais Player() e sim Player(self)
        pg.sprite.Sprite.__init__(self)
        self.game = game #Agora a classe Player tem como referência o jogo.
        self.walking = False
        self.jumping = False
        self.current_frame = 0
        self.last_update = 0
        self.load_images()
        self.dir = path.dirname(__file__)
        self.snd_dir = path.join(self.dir, 'snd')
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'fox_jump.wav'))
        self.image = self.standing_frame[0]
        self.image.set_colorkey(PLAYER_GREEN)
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH/2, 600)
        self.pos = vec(WIDTH/5, HEIGHT/2)
        self.vel = vec(0,0)
        self.acc = vec(0,0)

    def load_images(self):
        self.standing_frame = [self.game.fox_sprite.get_image(56, 4, 46, 35)]
        for frame in self.standing_frame:
            frame.set_colorkey(PLAYER_GREEN)
        self.walk_frame_r=[self.game.fox_sprite.get_image(0, 0, 45, 36),
                            self.game.fox_sprite.get_image(114, 2, 46, 36)]
        for frame in self.walk_frame_r:
            frame.set_colorkey(PLAYER_GREEN)
        self.walk_frame_l=[]
        for frame in self.walk_frame_r:
            frame.set_colorkey(PLAYER_GREEN)
            self.walk_frame_l.append(pg.transform.flip(frame, True, False))
        self.jump_frame = self.game.fox_sprite.get_image(229, 0, 38, 40)
        self.jump_frame.set_colorkey(PLAYER_GREEN)

    def jump(self):        
        #pular somente se estiver em uma plataforma ou estiver no chao
        self.rect.x += 1 #adicionei um pixel para o retângulo do jogador (verificar se tem ou não uma plataforma)
        hits = pg.sprite.spritecollide(self, self.game.platforms, False)
        self.rect.x -= 1 #retirei o pixel de verificação
        if hits:
            self.vel.y = -PLAYER_JUMP
            self.jump_sound.play()

    def update(self):
        self.animate()
        self.acc = vec(0,PLAYER_GRAVITY)
        keys = pg.key.get_pressed()
        if keys[pg.K_RIGHT]:
            self.acc.x = PLAYER_ACC
        
        # implementacao do atrito
        self.acc.x += self.vel.x * PLAYER_FRICTION
        #eq of motion
        self.vel += self.acc
        if abs(self.vel.x) < 0.1:
            self.vel.x = 0
        self.pos += self.vel + 0.5*self.acc
        # jogador sai pra fora da tela e volta do outro lado
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self. rect.midbottom = self.pos

    def animate(self):
        now = pg.time.get_ticks()
        if self.vel.x != 0:
            self.walking=True
        else:
            self.walking = False
        #animacao de andar
        if self.walking:
            if now - self.last_update>300:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.walk_frame_l)
                bottom = self.rect.bottom
                if self.vel.x>0:
                    self.image = self.walk_frame_r[self.current_frame]
                else:
                    self.image = self.walk_frame_l[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
        #animacao quando estiver parado
        if not self.jumping and not self.walking:
            if now - self.last_update > 200:
                self.last_update = now
                self.current_frame = (self.current_frame + 1) % len(self.standing_frame)
                bottom = self.rect.bottom
                self.image = self.standing_frame[self.current_frame]
                self.rect = self.image.get_rect()
                self.rect.bottom = bottom
            

class Platform(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        images = self.game.spritesheet.get_image(0, 288, 380, 94)
        self.image = images
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Spritesheet:
    #utility class for loading and parsing spritesheets
    def __init__(self, filename):
        self.spritesheet = pg.image.load(filename).convert()
        #self.cloud_spritesheet = pg.image.load(filename).convert()

    def get_image(self, x, y, w, h):
        # grab an image out of a larger spritesheet
        image = pg.Surface((w,h))
        image.blit(self.spritesheet, (0, 0), (x, y, w, h))
        image = pg.transform.scale(image, ((3*w)//4, (3*h)//4)) #resize image
        return image
        
class Mob(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        images = pg.image.load(path.join(mob_dir, 'lion_dir.png'))
        self.image = images
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y 

class Flag(pg.sprite.Sprite):
    def __init__(self, game, x, y):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        images = pg.image.load(path.join(mob_dir, 'flagRed.png'))
        self.image = images
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y