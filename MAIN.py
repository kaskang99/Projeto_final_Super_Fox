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
        # load hi-score
        self.dir = path.dirname(__file__)
        with open(path.join(self.dir, 'HS_FILE'), 'w') as f:
            try:
                self.highscore = int(f.read())
            except:
                self.highscore = 0
        #load spritesheet image
        self.fox_sprite = Spritesheet(path.join(img_dir, FOX_SPRITE))    
        self.spritesheet = Spritesheet(path.join(img_dir, SPRITESHEET))
        #load sounds
        self.snd_dir = path.join(self.dir, 'snd')
        self.jump_sound = pg.mixer.Sound(path.join(self.snd_dir, 'fox_jump.wav'))
        self.gameover_sound = pg.mixer.Sound(path.join(self.snd_dir, 'game_over.wav'))

    def new(self):
        # start a new game
        self.score = 0
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
        pg.mixer.music.load(path.join(self.snd_dir, 'game_music_theme.ogg'))
        pg.mixer.music.play(loops=-1)
        pg.mixer.music.set_volume(0.25)
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(500)

    def update(self):
        # Game update
        self.all_sprites.update()
        # verifica se o jogador colide com uma plataforma - somente quando estiver caindo
        if self.player.vel.y > 0:
            hits = pg.sprite.spritecollide(self.player, self.platforms, False)
            if hits:
                self.player.pos.y = hits[0].rect.top
                self.player.vel.y = 0
        #quando o jogador alcançar o terço da tela 
        if self.player.rect.right > WIDTH / 3:
            self.player.pos.x -= max(abs(self.player.vel.x),2)
            for plat in self.platforms:
                plat.rect.left -= max(abs(self.player.vel.x),2)
        elif self.player.rect.left < WIDTH / 4:
            self.player.pos.x += max(abs(self.player.vel.x),2)
            for plat in self.platforms:
                plat.rect.left += max(abs(self.player.vel.x),2)
        #jogador "cai" em um buraco e morre
        if self.player.rect.bottom > HEIGHT:
            self.playing = False
            self.gameover_sound.play()
            self.gameover_sound.set_volume(.2)

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
                    self.jump_sound.play()

    def draw(self):
        # Game loop - draw
        self.window.fill(SKYBLUE)
        self.all_sprites.draw(self.window)
        self.draw_text(str(self.score), 22, WHITE, WIDTH/2, 15)
        # after drawing everything, flip the display
        pg.display.flip()

    def show_start_screen(self):
        # game start screen
        pg.mixer.music.load(path.join(self.snd_dir, 'main_menu_music.ogg'))
        pg.mixer.music.play(loops=-1)
        self.window.fill(SKYBLUE)
        pg.mixer.music.set_volume(0.25)
        self.draw_text(TITLE, 48, BLACK, WIDTH/2, HEIGHT/4)
        self.draw_text("arrows to move, space to jump", 22, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text("Aperte qualquer tecla para começar", 22, BLACK, WIDTH/2, 3*HEIGHT/4)
        self.draw_text("Recorde: " +str(self.highscore), 22, YELLOW, WIDTH/2, 15)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(750)

    def show_go_screen(self):
        # game end screen
        if not self.running:
            return
        self.window.fill(TEAL)
        self.draw_text("GAME OVER", 48, BLACK, WIDTH/2, HEIGHT/2)
        self.draw_text("Pontuação: " +str(self.score), 22, WHITE, WIDTH/2, HEIGHT/5)
        self.draw_text("Aperte qualquer tecla para jogar novamente", 22, BLACK, WIDTH/2, 3*HEIGHT/4)
        if self.score > self.highscore:
            self.highscore = self.score
            self.draw_text("Parabéns! Você alcançou uma nova pontuação máxima!", 22, WHITE, WIDTH/2, HEIGHT/5 - 40)
            with open(path.join(self.dir, 'HS_FILE'), 'w') as f:
                f.write(str(self.score))
        else:
            self.draw_text("Recorde: " +str(self.highscore), 22, YELLOW, WIDTH/2, HEIGHT/6 - 40)
        self.draw_text("Aperte qualquer tecla para jogar novamente", 22, BLACK, WIDTH/2, 3*HEIGHT/4)
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