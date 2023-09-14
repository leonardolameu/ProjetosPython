import pygame, time

pygame.init()

janela = pygame.display.set_mode((500,500))
pygame.display.set_caption("Formas")

cor1 = (0, 0, 255)
cor2 = (255, 0, 0)
cor3 = (0, 255, 0)

largura = 100
altura = 200

x = 100
y = 300

run = True

while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.draw.rect(janela, (255, 255, 255), (10, 10, 20, 20))
    pygame.draw.rect(janela, cor1, (100, 50, 100, 100))
    pygame.draw.rect(janela, cor2, (200, 200, largura, altura))
    pygame.draw.circle(janela, cor3, (x, y), 130, 6)
    pygame.draw.polygon(janela, cor3, ((x + 200, y), (x + 300, y), (x + 250, y - 100)))
    pygame.display.update()


pygame.quit()