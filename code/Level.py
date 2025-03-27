import sys

import pygame as pg
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface

from code.Const import C_BLACK, WIN_HEIGHT
from code.Entity import Entity
from code.EntityFactory import EntityFactory


class Level:

    def __init__(self, window, name, game_mode):
        self.timeout = 0
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('Level1Bg'))
        self.player = EntityFactory.get_entity('Player',(5, WIN_HEIGHT / 1.55))
        self.entity_list.append(self.player)

    def run(self):
        pg.mixer_music.load(f'./asset/{self.name}.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()

            # Printando textos
            self.level_text(14, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_BLACK, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps() : .0f}', C_BLACK, (10, WIN_HEIGHT, -40))
            self.level_text(14, f'entidades: {len(self.entity_list)}', C_BLACK, (10, WIN_HEIGHT, -30))
            pg.display.flip()
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
