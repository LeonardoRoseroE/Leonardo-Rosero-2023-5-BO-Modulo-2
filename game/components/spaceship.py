import pygame
from pygame.sprite import Sprite

from game.utils.constants import SPACESHIP

# casi Todo en pygame es un objeto
# Un personaje en mi juego es un objeto (instancia de algo)
# La nave (spaceship) es un personaje => necesito una clase


# SpaceShip es una clase derivada (hija) de Sprite

# spaceship tiene una "imagen"
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
class SpaceShip(Sprite):
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.image_rect = self.image.get_rect()
        self.image_rect.x = self.image_size[0]
        self.image_rect.y = self.image_size[1]
    
    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a] and self.image_rect.left > 0:  # Tecla A para moverse a la izquierda
            self.image_rect.x -= 5
        if keys[pygame.K_d] and self.image_rect.right < SCREEN_WIDTH:  # Tecla D para moverse a la derecha
            self.image_rect.x += 5
        if keys[pygame.K_w] and self.image_rect.top > 0:  # Tecla W para moverse hacia arriba
            self.image_rect.y -= 5
        if keys[pygame.K_s] and self.image_rect.bottom < SCREEN_HEIGHT:  # Tecla S para moverse hacia abajo
            self.image_rect.y += 5