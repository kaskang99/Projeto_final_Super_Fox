#platform game

import pygame as pg
import os
from config import *
from sprites import *

class Game:
    def __init__(self):
        #initialize game window, etc
        pg.init()
        pg.mixer.init()

        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        
        
    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self) #da uma referencia para o jogo (um link para o jogo, mostra todas as variáveis do jogo e.g.: plataforma)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(*plat)
            self.all_sprites.add(p)
            self.platforms.add(p)
        self.run()

    def run(self):
        # Game loop
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
    
    def update(self):
        # Game update
        self.all_sprites.update()
        # verifica se o jogador colide com uma plataforma - somente quando estiver caindo
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        #quando o jogador alcançar a metade da tela 
        if self.player.rect.right > WIDTH / 2:
            self.player.pos.x -= max(abs(self.player.vel.x),2)
            for plat in self.platforms:
                plat.rect.right -= max(abs(self.player.vel.x),2)
        if self.player.rect.left < WIDTH / 2:
            self.player.pos.x += max(abs(self.player.vel.x),2)
            for plat in self.platforms:
                plat.rect.left += max(abs(self.player.vel.x),2)
        #jogador "cai" em um buraco e morre
        if self.player.rect.bottom > HEIGHT:
            self.playing = False
            self.running = False

    def events(self):
        # Game loop - events
        for event in pg.event.get():
        #check for closing window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE:
                    self.player.jump()

    def draw_grid(self):
        for x in range(0, WIDTH, TILESIZE):
            pg.draw.line(self.window, LIGHTGREY, (x,0), (x,HEIGHT))
        for y in range(0, HEIGHT, TILESIZE):
            pg.draw.line(self.window, LIGHTGREY, (0,y), (WIDTH,y))

    def draw(self):
        # Game loop - draw
        self.window.fill(BLACK)
        self.draw_grid()
        self.all_sprites.draw(self.window)

        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game start screen
        pass
    
    def show_go_screen(self):
        # game end screen)
        pass

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()