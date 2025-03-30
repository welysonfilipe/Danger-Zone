import random
import sys

import pygame as pg
from pygame.font import Font
from pygame.rect import Rect
from pygame.surface import Surface
from pygame.time import set_timer

from code.Const import C_BLACK, WIN_HEIGHT, WIN_WIDTH, EVENT_ENEMY, SPAWN_TIME, C_WHITE, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL
from code.Enemy import Enemy
from code.Entity import Entity
from code.EntityFactory import EntityFactory
from code.EntityMediator import EntityMediator
from code.Player import Player


class Level:

    def __init__(self, window: Surface, name: str, game_mode: str, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'Bg'))
        player = EntityFactory.get_entity('Player', (5, WIN_HEIGHT / 1.55))
        player.score = player_score[0]
        self.entity_list.append(player)
        pg.time.set_timer(EVENT_ENEMY, SPAWN_TIME)
        pg.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: int):
        pg.mixer_music.load(f'./asset/{self.name}.mp3')
        pg.mixer_music.play(-1)
        clock = pg.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player':
                    self.level_text(16, f'Player - health: {ent.health} | Score: {ent.score}', C_BLACK, (10, 25))
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    sys.exit()
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice, (WIN_WIDTH, WIN_HEIGHT / 1.55)))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0:
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player':
                                player_score[0] = ent.score
                        return True

                found_player = False

                for ent in self.entity_list:
                    if isinstance(ent, Player):
                        found_player = True

                if not found_player:
                    return False

            # Printando textos
            self.level_text(16, f'{self.name} - Timeout: {self.timeout / 1000 :.1f}s', C_BLACK, (10, 5))
            self.level_text(16, f'fps: {clock.get_fps() :.0f}', C_WHITE, (10, WIN_HEIGHT - 30))
            self.level_text(16, f'entidades: {len(self.entity_list)}', C_WHITE, (10, WIN_HEIGHT - 20))
            pg.display.flip()
            # Colisão
            EntityMediator.verify_collision(entity_list=self.entity_list)  # Verificando colisão
            EntityMediator.verify_health(entity_list=self.entity_list)  # Verificando a vida
        pass

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pg.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
