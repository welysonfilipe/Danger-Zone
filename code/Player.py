import pygame as pg

from code.Const import WIN_HEIGHT, WIN_WIDTH, ENTITY_SPEED, PLAYER_KEY_SHOOT, ENTITY_SHOOT_DELAY
from code.Entity import Entity
from code.PlayerShot import PlayerShot


class Player(Entity):

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
        self.is_jumping = False
        self.jump_speed = -15  # Velocidade inicial do salto
        self.gravity = 1  # Gravidade para acelerar a descida
        self.vertical_speed = 0
        self.last_frame_update = pg.time.get_ticks()  # Marca o tempo do último frame trocado
        self.frame_delay = 100
        self.shot_delay = ENTITY_SHOOT_DELAY[self.name]

    def move(self):
        pressed_key = pg.key.get_pressed()
        now = pg.time.get_ticks()  # Tempo atual

        moving = False  # Verificar se o personagem está em movimento

        # Movimentos horizontais
        if pressed_key[pg.K_LEFT]:
            self.rect.x -= ENTITY_SPEED[self.name]
            moving = True

        elif pressed_key[pg.K_RIGHT]:
            self.rect.x += ENTITY_SPEED[self.name]
            moving = True

        # Atualizar o frame apenas após o intervalo definido
        if moving and now - self.last_frame_update > self.frame_delay:
            self.last_frame_update = now
            self.current_frame = (self.current_frame + 1) % len(self.frames)
            self.surf = self.frames[self.current_frame]

        # Garantindo que o personagem não ultrapasse os limites da tela
        self.rect.x = max(0, min(self.rect.x, WIN_WIDTH - self.surf.get_width()))

        # Verificando o salto
        if pressed_key[pg.K_UP] and not self.is_jumping:
            self.is_jumping = True
            self.vertical_speed = self.jump_speed

        # Atualizando a posição
        if self.is_jumping:
            self.rect.y += self.vertical_speed
            self.vertical_speed += self.gravity

            # Verificando se atingiu o chão
            if self.rect.y >= WIN_HEIGHT / 1.55:
                self.rect.y = WIN_HEIGHT / 1.55
                self.is_jumping = False
                self.vertical_speed = 0
        pass

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOOT_DELAY[self.name]
            pressed_key = pg.key.get_pressed()
            if pressed_key[PLAYER_KEY_SHOOT[self.name]]:
                shot_x = self.rect.left + 50
                shot_y = self.rect.top + 25
                return PlayerShot(name=f'{self.name}Shot', position=(shot_x, shot_y))
