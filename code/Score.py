import sys
from datetime import datetime

import pygame as pg
from pygame.constants import KEYDOWN, K_RETURN, K_BACKSPACE, K_ESCAPE
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import WIN_WIDTH, WIN_HEIGHT, C_YELLOW, SCORE_POS, C_WHITE, C_BLACK, MENU_OPTION
from code.DBProxy import DBProxy


class Score:

    def __init__(self, window: Surface):
        self.window = window
        self.surf = pg.image.load('./asset/ScoreBg.png').convert_alpha()
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

    def save(self, game_mode: str, player_score: list[int]):
        pg.mixer_music.load('./asset/Score.aiff')
        pg.mixer_music.play(-1)
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf_ajustado, dest=self.rect)
            self.score_text(58, 'VOCÊ GANHOU!!', C_WHITE, SCORE_POS['Title'])
            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                text = 'Player digite o seu nome (4 caracteres):'
            self.score_text(36, text, C_WHITE, SCORE_POS['EnterName'])


            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key == K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(28, name, C_WHITE, SCORE_POS['Name'])
            pg.display.flip()
            pass

    def show(self):
        pg.mixer_music.load('./asset/Score.aiff')
        pg.mixer_music.play(-1)
        self.window.blit(source=self.surf_ajustado, dest=self.rect)
        self.score_text(58, 'TOP 10 SCORE', C_WHITE, SCORE_POS['Title'])
        self.score_text(30,'NAME      SCORE         DATE      ', C_WHITE, SCORE_POS['Label'])
        db_proxy = DBProxy('DBScore')
        list_score = db_proxy.retrieve_top10()
        db_proxy.close()

        for player_score in list_score:
            id_, name, score, date = player_score
            self.score_text(24,f'{name}         {score :05d}        {date}', C_WHITE,
                           SCORE_POS[list_score.index(player_score)])
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        return
            pg.display.flip()


    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)

def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"