import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH

class SpaceShip(Sprite):
    def __init__(self):
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.image_size[0]
        self.image_rect.y = self.image_size[1]
        self.screen_width = pygame.display.get_surface().get_width()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Tecla A para moverse a la izquierda
            self.image_rect.x -= 7
            if self.image_rect.right < 0:
                self.image_rect.left = self.screen_width
        if keys[pygame.K_d]:  # Tecla D para moverse a la derecha
            self.image_rect.x += 7
            if self.image_rect.left > self.screen_width:
                self.image_rect.right = 0
        if keys[pygame.K_w] and self.image_rect.top > 0:  # Tecla W para moverse hacia arriba
            self.image_rect.y -= 7
        if keys[pygame.K_s] and self.image_rect.bottom < SCREEN_HEIGHT:  # Tecla S para moverse hacia abajo
            self.image_rect.y += 7
