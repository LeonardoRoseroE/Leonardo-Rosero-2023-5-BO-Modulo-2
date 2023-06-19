import pygame
from game.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT, MENU

class Menu:
    def __init__(self):
        self.selected_option = None
    
    def run(self):
        pygame.init()
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Menú")

        font = pygame.font.Font(None, 36)
        play_text = font.render("Jugar", True, (255, 255, 255))
        #instructions_text = font.render("Instrucciones", True, (255, 255, 255))
        exit_text = font.render("Salir", True, (255, 255, 255))

        while not self.selected_option:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    return

                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    if play_button_rect.collidepoint(mouse_pos):
                        self.selected_option = "Jugar"
                        pygame.time.delay(200)  # Agrega un retraso de 200 milisegundos

                    # elif instructions_button_rect.collidepoint(mouse_pos):
                    #     self.show_instructions()
                    #     pygame.time.delay(200)  # Agrega un retraso de 200 milisegundos

                    elif exit_button_rect.collidepoint(mouse_pos):
                        pygame.quit()
                        return

            screen.blit(MENU, (0, 0))  # Dibujar imagen de fondo del menú
            play_button_rect = screen.blit(play_text, (SCREEN_WIDTH // 2 - 50, SCREEN_HEIGHT // 2 - 50))
            #instructions_button_rect = screen.blit(instructions_text, (SCREEN_WIDTH // 2 - 75, SCREEN_HEIGHT // 2))
            exit_button_rect = screen.blit(exit_text, (SCREEN_WIDTH // 2 - 40, SCREEN_HEIGHT // 2 + 50))

            pygame.display.flip()

    def show_instructions(self):
        # Implementa aquí la lógica para mostrar las instrucciones
        pass


