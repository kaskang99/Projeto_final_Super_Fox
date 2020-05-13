# Projeto_final_Super_Fox
The game was developed as a final assignment for a class called Software Design.

Objetivo:
	Desenvolver um jogo de computador em Python 3 usando recursos da biblioteca PyGame.
	
    O jogo deverá ser interativo:
		permitir que um ou mais jogadores interajam em um jogo
		ter um objetivo final bem definido
	
	O desenvolvimento deverá ser feito em grupos de 2 ou 3 alunos, todos usando um sistema de versionamento de Git.
	
    O tema do jogo é livre, contudo, a proposta deve ser previamente discutida com o professor.

Descrição:

Como instalar as bibliotecas utilizadas:
	
    Pygame:
	
    	linux ou windows:
	
    		no terminal Anaconda Prompt (se estiver utilizando o distribuidor Anaconda), digite "pip install pygame" (sem as aspas) e aperte a tecla "enter".
	
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
	