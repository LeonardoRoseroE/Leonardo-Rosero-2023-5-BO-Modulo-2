import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT,END

class GameOver:
    def __init__(self):
        self.font = pygame.font.Font(None, 36)
    
    def draw(self, screen, bullet_count, death_count):
        screen.blit(END,(0,0))
        text = self.font.render("GAME OVER", True, (255, 0, 0))
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(text, text_rect)

        bullet_count_text = self.font.render(f"Bullet Count: {bullet_count}", True, (255, 255, 255))
        bullet_count_rect = bullet_count_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(bullet_count_text, bullet_count_rect)

        death_count_text = self.font.render(f"Attempts Count: {death_count}", True, (255, 255, 255))
        death_count_rect = death_count_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(death_count_text, death_count_rect)

        pygame.display.flip()