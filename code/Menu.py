import pygame as pg
import pygame.image
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, WIN_HEIGHT


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
        self.surf_ajustado = pg.transform.smoothscale(self.surf,(nova_largura, nova_altura))

        # Centralizando a imagem na tela
        pos_x = (WIN_WIDTH - nova_largura) // 2
        pos_y = (WIN_HEIGHT - nova_altura) // 2

    def run(self, ):
        pg.mixer_music.load('./asset/menu.aiff')
        pg.mixer_music.play(-1)
        while True:
            self.window.blit(source=self.surf_ajustado, dest=self.rect)
            self.menu_text(60, "ZOMBIELAND", (205, 92, 92), ((WIN_WIDTH / 2), 70))
            pg.display.flip()
             # Checando todos os eventos
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()  # Fechando a janela
                    quit()  # Fechando o pygame

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)