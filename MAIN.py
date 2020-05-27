#platform game

import pygame as pg
import os
from config import *
from sprites import *
from assets import *
from game_screen import *
from os import path

class Game:
    def __init__(self):
        #initialize game window, etc
        pg.init()
        pg.mixer.init()

        self.window = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption(TITLE)
        self.clock = pg.time.Clock()
        self.running = True
        self.font_name = pg.font.match_font(FONT)    
        self.load_data()

    def load_data(self):
        self.dir = path.dirname(__file__)
        img_dir = path.join(self.dir, 'SpriteSheets')

        #load spritesheet image
        self.fox_sprite = Spritesheet(path.join(img_dir, FOX_SPRITE))    
         
    def new(self):
        # start a new game
        self.all_sprites = pg.sprite.Group()
        self.platforms = pg.sprite.Group()
        self.player = Player(self) #da uma referencia para o jogo (um link para o jogo, mostra todas as variáveis do jogo e.g.: plataforma)
        self.all_sprites.add(self.player)
        for plat in PLATFORM_LIST:
            p = Platform(self, *plat)
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
        if self.player.rect.right > WIDTH / 3:
            self.player.pos.x -= max(abs(self.player.vel.x),2)
            for plat in self.platforms:
                plat.rect.right -= max(abs(self.player.vel.x),2)
        if self.player.rect.left < WIDTH / 3:
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
        self.window.fill(TEAL)
        self.draw_grid()
        self.all_sprites.draw(self.window)

        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game start screen
        self.window.fill(TEAL)
        self.draw_text(TITLE, 48, BLACK, WIDTH/2, HEIGHT/4)
        self.draw_text("arrows to move, space to jump", 22, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text("aperte qualquer tecla para começar", 22, BLACK, WIDTH/2, 3*HEIGHT/4)
        pg.display.flip()
        self.wait_for_key()

    def show_go_screen(self):
        # game end screen
        if not self.running:
            return
        self.window.fill(TEAL)
        self.draw_text("GAME OVER", 48, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text("aperte qualquer tecla para jogar novamente", 22, BLACK, WIDTH/2, 3*HEIGHT/4)
        pg.display.flip()
        self.wait_for_key()

    def wait_for_key(self):
        waiting = True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    waiting = False
                    self.running = False
                if event.type == pg.KEYUP:
                    waiting = False

    def draw_text(self, text, size, color, x , y):
        font = pg.font.Font(self.font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.window.blit(text_surface, text_rect)

g = Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()