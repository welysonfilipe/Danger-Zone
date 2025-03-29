from abc import ABC, abstractmethod
import pygame as pg
import pygame.image

from code.Const import WIN_WIDTH, WIN_HEIGHT, ENTITY_HEALTH, ENTITY_DAMAGE


class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pg.image.load('./asset/' + name + '.png').convert_alpha()

        # Obtendo dimensões originais
        largura_imagem, altura_imagem = self.surf.get_size()
        nova_largura = largura_imagem
        nova_altura = altura_imagem

        if largura_imagem > 100 and altura_imagem > 100: # Apenas redimensionar imagens grandes
            # Mantendo a proporção em relação à janela
            proporcao_largura = WIN_WIDTH / largura_imagem
            proporcao_altura = WIN_HEIGHT / altura_imagem
            proporcao = min(proporcao_largura, proporcao_altura)

            nova_largura = int(largura_imagem * proporcao)
            nova_altura = int(altura_imagem * proporcao)

            # Redimensionando a imagem
            self.surf = pg.transform.smoothscale(self.surf, (nova_largura, nova_altura))

        # Centralizando a imagem na tela
        pos_x = (WIN_WIDTH - nova_largura) // 2
        pos_y = (WIN_HEIGHT - nova_altura) // 2

        self.rect = self.surf.get_rect(left=position[0], top=position[1])
        self.speed = 0
        self.health = ENTITY_HEALTH[self.name]
        self.damage = ENTITY_DAMAGE[self.name]
        self.last_dmg = 'None'

    @abstractmethod
    def move(self, ):
        pass