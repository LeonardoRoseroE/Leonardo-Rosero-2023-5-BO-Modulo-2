import pygame
from pygame.sprite import Sprite
from game.utils.constants import BULLET_SPEED, BULLET

class Bullet(Sprite):
    def __init__(self, x, y, velocity_x=0, velocity_y=0):
        super().__init__()
        self.image = pygame.transform.scale(BULLET, (10, 20))  # Ajusta el tamaño de la imagen
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.velocity_x = velocity_x
        self.velocity_y = velocity_y


    def update(self):
        self.rect.x += self.velocity_x
        self.rect.y += self.velocity_y