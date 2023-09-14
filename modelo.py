import pygame
import random

#load/carregar
pygame.init()
janela = pygame.display.set_mode((640, 480))
pygame.display.set_caption("Projeto Base")
clock = pygame.time.Clock()
FPS = 60

velocidadeX = random.randint(-3, 3)


#inicio do ciclo
run = True
white run:
    #update/atualização
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False


            #draw/apresentação

            pygame.display.update()


#fechamento do jogo
pygame.quit()