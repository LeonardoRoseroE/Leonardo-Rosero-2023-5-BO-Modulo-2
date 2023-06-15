import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET_SPEED, BULLET

class Bullet(Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.transform.scale(BULLET, (10, 20))  # Ajusta el tamaño de la imagen
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        self.rect.y -= BULLET_SPEED
