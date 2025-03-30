import pygame as pg

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION
from code.Level import Level
from code.Menu import Menu


class Game:
    def __init__(self):
        pg.init()
        # Criando uma janela
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            if menu_return == MENU_OPTION[0]:
                player_score = [0]
                level = Level(self.window, 'Level1', menu_return, player_score)
                level_return = level.run(player_score)
                if level_return:
                    level = Level(self.window, 'Level2', menu_return, player_score)
                    level_return = level.run(player_score)

            elif menu_return == MENU_OPTION[2]:
                pg.quit() # Fecha a janela
                quit() # Termina o pygame
            else:
                pass

