import pygame
from pygame.sprite import Sprite
from random import randint
from game.utils.constants import SCREEN_WIDTH, SHIELD, FPS
from game.components.spaceship import SpaceShip

MOV = 2
immune_duration = 30 * FPS  # Duración de la inmunidad en ticks

class Shield(Sprite):
     
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(SHIELD, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2  # Posicionar en el centro horizontal
        self.rect.y = 450  # Posicionar en la parte superior de la pantalla
        self.speed = 0  # Velocidad de movimiento
        self.target_x = self.rect.x  # Posición objetivo inicial
        self.bullets = pygame.sprite.Group()  # Grupo para almacenar las balas
        self.last_shot_time = 0 # Variable para almacenar el tiempo entre balas

    def reset(self):
        self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 450
       


    def update(self, spaceship_rect):
        target_x = spaceship_rect.x - self.rect.width // 2

        # Calcular la interpolación lineal
        if self.rect.x < target_x:
            self.rect.x += min(self.speed, target_x - self.rect.x)
        elif self.rect.x > target_x:
            self.rect.x -= min(self.speed, self.rect.x - target_x)

        # Actualizar la posición objetivo
        self.target_x = target_x


    def activate(self, duration=30 * FPS):
        self.alive = True
        self.timer = duration
        

    def deactivate(self):
        self.alive = False
        self.timer = 0
    
    def is_active(self):
        return self.activate
        
    def reset_position(self):
        self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 250
