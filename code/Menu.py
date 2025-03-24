import pygame as pg
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, WIN_HEIGHT, MENU_OPTION, C_WHITE, C_YELLOW, C_ORANGE


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pg.image.load('./asset/MenuBg.png')
        self.rect = self.surf.get_rect(left=0, top=0)

        # Obtendo as dimensões originais da imagem
        largura_imagem, altura_imagem = self.surf.get_size()

        # Calculando a proporção para ajustar o tamanho da janela
        proporcao_largura = WIN_WIDTH / largura_imagem
        proporcao_altura = WIN_HEIGHT / altura_imagem
        proporcao = min(proporcao_largura, proporcao_altura)

        # Calculando as novas dimensões da imagem e mantendo a proporção
        nova_largura = int(largura_imagem * proporcao)
        nova_altura = int(altura_imagem * proporcao)

        # Redimensionando a imagem
        self.surf_ajustado = pg.transform.smoothscale(self.surf, (nova_largura, nova_altura))

        # Centralizando a imagem na tela
        pos_x = (WIN_WIDTH - nova_largura) // 2
        pos_y = (WIN_HEIGHT - nova_altura) // 2

    def run(self, ):
        menu_option = 0
        pg.mixer_music.load('./asset/menu.aiff')
        pg.mixer_music.play(-1)
        while True:
            # Desenhando as imagens
            self.window.blit(source=self.surf_ajustado, dest=self.rect)
            self.menu_text(75, "DANGER", (C_YELLOW), ((WIN_WIDTH / 2), 70))
            self.menu_text(65, "ZONE", (C_YELLOW), ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(35, MENU_OPTION[i], (C_ORANGE), ((WIN_WIDTH / 2), 250 + 30 * i))
                else:
                    self.menu_text(35, MENU_OPTION[i], (C_WHITE), ((WIN_WIDTH / 2), 250 + 30 * i))
            pg.display.flip()

            # Checando todos os eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # Fechando a janela
                    quit()  # Fechando o pygame
                if event.type == pg.KEYDOWN:
                    if event.key == pg.K_DOWN:  # Seta pra baixo
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0
                    if event.key == pg.K_UP:  # Seta pra cima
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pg.K_RETURN:  # Enter
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
