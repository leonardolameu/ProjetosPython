import pygame, time

pygame.init()
janela = pygame.display.set_mode((600, 300))
fonte = pygame.font.SysFont("Arial", 60)
texto = fonte.render("Olá Mundo!", 1, (255, 255, 255))

janela.blit(texto, (125, 100))
pygame.display.update()
time.sleep(5)
pygame.quit()