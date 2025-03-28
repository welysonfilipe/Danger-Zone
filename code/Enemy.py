import pygame as pg

from code.Const import WIN_WIDTH
from code.Entity import Entity


class Enemy(Entity):

    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)

        # Carregar a imagem completa
        full_image = pg.image.load(f'./asset/' + name + '.png').convert_alpha()

        # Encontrando as dimensões de cada frame
        num_frames = 10
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

    def move(self, ):
        self.rect.x -= 1

