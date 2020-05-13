import pygame

pygame.init() #pygame iniciado

# ----- Gera tela principal
window = pygame.display.set_mode((800, 600)) #cria uma janela com 500 pixels de largura e 400 pixels de altura
pygame.display.set_caption('Super FOX') #define o titulo da janela como o texto "Hello World!"

# ----- Inicia estruturas de dados
game = True #a variável game será utilizada para indicar que o jogo deve continuar

# ===== Loop principal =====
while game: #enquanto game for true
    # ----- Trata eventos
    for event in pygame.event.get(): #pygame.event.get() - devolve uma lista com todos os eventos (clicks, mouse mvmnt, teclas apertadas, botoes da janela apertados, etc)
        # ----- Verifica consequências
        if event.type == pygame.KEYUP: #pygame.KEYUP se o usuário apertar uma teclado do teclado, a janela é fechada
            game = False
    # ----- Gera saídas
    window.fill((135, 206, 235))  # Preenche com a cor escolhida, RGB (Red, Green, Blue) que variam entre 0 e 255.
    marrom_chao = (139, 69, 19)
    chao_vertices = [(0, 600), (800, 600), (800,400), (0,400)]
    verde_grass = (11, 102, 35)
    grass_vertices = [(0, 400), (800, 400), (800, 450), (0,450)]
    pygame.draw.polygon(window, marrom_chao, chao_vertices)
    pygame.draw.polygon(window, verde_grass, grass_vertices)
    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()