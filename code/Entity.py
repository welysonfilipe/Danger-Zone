from abc import ABC, abstractmethod
import pygame as pg
import pygame.image

class Entity(ABC):

    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pg.image.load('./asset' + name + '.png')
        self.rect = self.surf.getrect(left=position[0], top=position[1])
        self.speed = 0

    @abstractmethod
    def move(self, ):
        pass