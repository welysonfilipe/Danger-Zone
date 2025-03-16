import pygame as pg

from code.Menu import Menu


class Game:
    def __init__(self):
        pg.init()
        # Criando uma janela
        self.window = pg.display.set_mode(size=(600, 480))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            #  # Checando todos os eventos
            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()  # Fechando a janela
            #         quit()  # Fechando o pygame
