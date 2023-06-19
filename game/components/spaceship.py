import pygame
from pygame.sprite import Sprite
from game.components.bullet import Bullet
from game.utils.constants import SPACESHIP, SCREEN_HEIGHT, SCREEN_WIDTH, FPS

MOV = 7

class SpaceShip(Sprite):

    immune_duration = 30 * FPS  # Duración de la inmunidad en ticks

    def __init__(self):
        super().__init__()
        self.immune_timer = 0  # Timer de inmunidad inicializado en 0
        self.image_size = (40, 60)
        self.image = pygame.transform.scale(SPACESHIP, self.image_size)
        self.rect = self.image.get_rect()
        self.rect.x = SCREEN_WIDTH // 2
        self.rect.y = SCREEN_HEIGHT // 2
        self.screen_width = pygame.display.get_surface().get_width()
        self.bullets = pygame.sprite.Group()

    def activate_immunity(self):
        self.immune_timer = self.immune_duration

    def get_immune_time(self):
        return max(self.immune_timer // FPS, 0)  # Convierte los ticks restantes a segundos y asegura que sea un valor no negativo

    def is_immune(self):
        return self.immune_timer > 0
    
    def reset(self):
        self.rect.centerx = SCREEN_WIDTH // 2
        self.rect.bottom = SCREEN_HEIGHT - 20
        self.speed = 0
        self.bullets.empty()

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:  # Tecla A para moverse a la izquierda
            self.rect.x -= MOV
            if self.rect.right < 0:
                self.rect.left = self.screen_width
        if keys[pygame.K_d]:  # Tecla D para moverse a la derecha
            self.rect.x += MOV
            if self.rect.left > self.screen_width:
                self.rect.right = 0
        if keys[pygame.K_w] and self.rect.top > 0:  # Tecla W para moverse hacia arriba
            self.rect.y -= MOV
        if keys[pygame.K_s] and self.rect.bottom < SCREEN_HEIGHT:  # Tecla S para moverse hacia abajo
            self.rect.y += MOV

        if keys[pygame.K_SPACE]:  # Tecla Espacio para disparar
            self.shoot()

        if self.immune_timer > 0:
            self.immune_timer -= 1

        self.bullets.update()

    def shoot(self):
        bullet = Bullet(self.rect.centerx, self.rect.top, velocity_x=0 , velocity_y= -10)
        self.bullets.add(bullet)

    @property

    def image_rect(self):
        return self.rect

