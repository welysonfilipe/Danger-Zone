import pygame as pg

from code.Const import WIN_WIDTH, ENTITY_SPEED, ENTITY_SHOOT_DELAY
from code.EnemyShot import EnemyShot
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Carregar a imagem completa
        full_image = pg.image.load(f'./asset/' + name + '.png').convert_alpha()

        # Encontrando as dimensões de cada frame
        num_frames = 4
        frame_width = full_image.get_width() // num_frames
        frame_height = full_image.get_height()

        # Dividindo os frames
        self.frames = [
            full_image.subsurface((i * frame_width, 0, frame_width, frame_height)).convert_alpha()
            for i in range(num_frames)
        ]

        # Inicializando com o primeiro frame
        self.current_frame = 0
        self.surf = self.frames[self.current_frame]
        self.shot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self, ):
        self.rect.x -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOOT_DELAY[self.name]

            # Definição dos ajustes de posição para cada tipo de inimigo
            if self.name == "Enemy1":
                shot_x = self.rect.left + 10  # Ajuste horizontal para Enemy1
                shot_y = self.rect.top + 25  # Ajuste vertical para Enemy1
            elif self.name == "Enemy2":
                shot_x = self.rect.left + 10  # Ajuste horizontal para Enemy2
                shot_y = self.rect.top + 15  # Ajuste vertical para Enemy2
            else:
                # Posição padrão caso o inimigo não esteja listado
                shot_x = self.rect.centerx
                shot_y = self.rect.centery

            return EnemyShot(name=f'{self.name}Shot', position=(shot_x, shot_y))


