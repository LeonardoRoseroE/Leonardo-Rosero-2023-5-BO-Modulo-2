import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, WHITE

class GameOver:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)

    def draw(self, screen, bullet_count, death_count):
        screen.fill(WHITE)
        text = self.font.render("Game Over", True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        bullet_count_text = self.font.render(f"Bullet Count: {bullet_count}", True, (0, 0, 0))
        bullet_count_rect = bullet_count_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(bullet_count_text, bullet_count_rect)

        death_count_text = self.font.render(f"Death Count: {death_count}", True, (0, 0, 0))
        death_count_rect = death_count_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(death_count_text, death_count_rect)

        pygame.display.flip()
