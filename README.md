# Projeto_final_Super_Fox
Criadores:
    Bruno Boldrim Saboya
    Lucas Kang
    Murilo Prado Weyne

EXECUTAR O ARQUIVO:
    MAIN.py

Vídeo do jogo rodando:
https://www.youtube.com/watch?v=dRAPQ9eIPGY

The game was developed as a final assignment for a class called Software Design.

Objetivo do projeto:
	Desenvolver um jogo de computador em Python 3 usando recursos da biblioteca PyGame.
	
    O jogo deverá ser interativo:
		permitir que um ou mais jogadores interajam em um jogo
		ter um objetivo final bem definido
	
	O desenvolvimento deverá ser feito em grupos de 2 ou 3 alunos, todos usando um sistema de versionamento de Git.
	
    O tema do jogo é livre, contudo, a proposta deve ser previamente discutida com o professor.

Descrição do jogo:
    O jogo foi inspirado pelas teorias Nihilistas, aonde nada na vida tem sentido ou propósito.
    Todos os esforços para completar a fase são em vão, e mesmo após a morte, o highscore não é armazenado em uma tentativa de ilustrar a triste realidade que vivemos.
    Toda decisão tomada se torna passado, ou seja, não tem como voltar para trás.

Como instalar as bibliotecas utilizadas:
	
    Pygame:
    	linux ou windows:
    		no terminal Anaconda Prompt (se estiver utilizando o distribuidor Anaconda), digite "pip3 install pygame" (sem as aspas) e aperte a tecla "enter".
    	Mac OSX:
    		Se não tiver o Homebrew instalado, instale-o seguindo as instruções disponíveis no link https://brew.sh/
    		Abra o terminal e digite:
    			
                brew install sdl2 sdl2_gfx sdl2_image 
                sdl2_mixer sdl2_net sdl2_ttf
                brew install Caskroom/cask/xquartz
                git clone -b 1.9.6 --single-branch https://
                github.com/pygame/pygame.git
                cd pygame
                python setup.py -config -auto -sdl2
                python setup.py install
                cd ..
                rm -rf pygame
	