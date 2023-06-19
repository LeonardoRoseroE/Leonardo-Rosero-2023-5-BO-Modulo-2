import pygame
from game.components.menu import Menu
from game.components.game import Game

if __name__ == "__main__":
    pygame.init()
    pygame.display.set_caption("Juego")
    menu = Menu()
    menu.run()

    if menu.selected_option == "Jugar":
        game = Game()
        game.run()
 
    pygame.quit()