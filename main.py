import pygame as pg

pg.init()

# Criando uma janela
window = pg.display.set_mode(size = (600, 480))

while True:
    # Checando todos os eventos
    for event in pg.event.get():
        if event.type == pg.QUIT:
            pg.quit() # Fechando a janela
            quit() # Fechando o pygame
