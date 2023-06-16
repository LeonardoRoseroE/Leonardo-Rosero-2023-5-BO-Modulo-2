import pygame
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS, DEFAULT_TYPE
from game.components.spaceship import SpaceShip
from game.components.enemy import Enemy

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = 0
        self.y_pos_bg = 0
        self.bullet_count = 0
        self.death_count = 0

        self.spaceship = SpaceShip()
        self.enemy = Enemy()

    def run(self):
        self.playing = True
        while self.playing:
            self.handle_events()
            self.update()
            self.draw()
        
        self.show_game_over_screen()

        pygame.display.quit()
        pygame.quit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        self.spaceship.update()
        self.enemy.update(self.spaceship.rect)  

        # Verificar colisiones entre las balas del spaceship y el enemigo
        collisions = pygame.sprite.spritecollide(self.enemy, self.spaceship.bullets, True)
        if collisions:
            self.enemy.reset_position()
            self.bullet_count += 1

        if self.bullet_count > 5:  
            self.game_over = True
            self.death_count += 1

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.screen.blit(self.spaceship.image, self.spaceship.rect)
        self.screen.blit(self.enemy.image, self.enemy.rect)
        self.spaceship.bullets.draw(self.screen)
        self.enemy.bullets.draw(self.screen)
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image = pygame.transform.scale(BG, (SCREEN_WIDTH, SCREEN_HEIGHT))
        image_height = image.get_height()
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
        if self.y_pos_bg >= SCREEN_HEIGHT:
            self.screen.blit(image, (self.x_pos_bg, self.y_pos_bg - image_height))
            self.y_pos_bg = 0
        self.y_pos_bg += self.game_speed

    def show_game_over_screen(self):
        font = pygame.font.Font(None, 64)
        game_over_text = font.render("Game Over", True, (255, 0, 0))
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        summary_text = font.render(f"Bullets: {self.bullet_count}", True, (0, 0, 0))
        summary_rect = summary_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        death_count_text = font.render(f"Death Count: {self.death_count}", True, (0, 0, 0))
        death_count_rect = death_count_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))

        self.screen.fill((255, 255, 255))
        self.screen.blit(game_over_text, game_over_rect)
        self.screen.blit(summary_text, summary_rect)
        self.screen.blit(death_count_text, death_count_rect)
        pygame.display.flip()
        pygame.time.wait(3000)  # Muestra la pantalla de Game Over durante 3 segundos

