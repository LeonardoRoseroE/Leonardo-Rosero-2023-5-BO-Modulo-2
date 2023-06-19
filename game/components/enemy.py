import pygame
from pygame.sprite import Sprite
from random import randint
from game.utils.constants import SCREEN_WIDTH, ENEMY_1
from game.components.bullet import Bullet

MOV = 5

class Enemy(Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(ENEMY_1, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2 - self.rect.width // 2  # Posicionar en el centro horizontal
        self.rect.y = 100  # Posicionar en la parte superior de la pantalla
        self.speed = 6  # Velocidad de movimiento
        self.target_x = self.rect.x  # Posición objetivo inicial
        self.bullets = pygame.sprite.Group()  # Grupo para almacenar las balas
        self.last_shot_time = 0 # Variable para almacenar el tiempo entre balas

    def reset(self):
        self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 100
       


    def update(self, spaceship_rect):
        target_x = spaceship_rect.x - self.rect.width // 2

        # Calcular la interpolación lineal
        if self.rect.x < target_x:
            self.rect.x += min(self.speed, target_x - self.rect.x)
        elif self.rect.x > target_x:
            self.rect.x -= min(self.speed, self.rect.x - target_x)

        # Actualizar la posición objetivo
        self.target_x = target_x

        # Disparar una bala automáticamente
        self.shoot()

        # Actualizar las balas
        self.bullets.update()

    def shoot(self):
        current_time = pygame.time.get_ticks()
        time_since_last_shot = current_time - self.last_shot_time
        if time_since_last_shot >= 1500:  # 1500 milisegundos = 1.5 segundos
            bullet = Bullet(self.rect.centerx, self.rect.bottom, velocity_x=0, velocity_y=5)
            self.bullets.add(bullet)
            self.last_shot_time = current_time

    def reset_position(self):
        self.rect.x = randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 80



