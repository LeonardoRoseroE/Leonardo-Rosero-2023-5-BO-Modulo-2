import pygame
import pygame.font
from game.utils.constants import BG, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, TITLE, FPS
from game.components.spaceship import SpaceShip
from game.components.enemy import Enemy
from game.components.enemy_2 import Enemy_2
from game.components.end import GameEnd
from game.components.menu import Menu
from game.components.gameover import GameOver
from game.components.shield import Shield
defaul = 0


class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.font = pygame.font.Font(None, 36)  # Fuente y tamaño del texto del puntaje
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.game_speed = 10
        self.x_pos_bg = defaul
        self.y_pos_bg = defaul
        self.bullet_count = defaul
        self.death_count = defaul
        self.score = defaul
        self.play_count = defaul
        self.play_count_enemy = defaul
        self.score = defaul # inicializamos el puntaje en 0 

        self.shield_active_timer = 0  # Tiempo restante hasta que el escudo vuelva a aparecer


        self.spaceship = SpaceShip()
        self.shield = Shield()
        self.enemy = Enemy()
        self.enemy_2 = Enemy_2 ()
    
    def increase_play_score(self):
        self.score += 100

        
    def reset(self):
        self.spaceship.reset()  # Reiniciar la nave espacial
        self.shield.reset() # REiniciamos el Escudo
        self.score = defaul
        self.shield_active_timer = 0
        self.enemy.reset()  # Reiniciar el enemigo
        self.enemy_2.reset() # Reiniciamos el enemigo 2
        self.spaceship.bullets.empty()  # Vaciar las balas del jugador
        self.enemy.bullets.empty()  # Vaciar las balas del enemigo
        self.bullet_count = 0  # Reiniciar el contador de balas
        # self.death_count = 0  # Reiniciar el contador de muertes

    def show_menu_screen(self):
        menu = Menu()
        menu.run()
        self.reset()
        self.bullet_count = 0
        self.bullet_count_enemy = 0
        self.death_count += 1
      

    def show_game_end_screen(self):
        game_end = GameEnd()
        game_end.draw(self.screen, self.bullet_count, self.death_count, self.score)
        pygame.display.flip()
        pygame.display.flip()
        pygame.time.wait(3000)
    
    def show_game_over_screen(self):
        game_end = GameOver()
        game_end.draw(self.screen, self.bullet_count_enemy, self.death_count)
        pygame.display.flip()
        pygame.display.flip()
        pygame.time.wait(3000)

    def run(self):
        while True:
            self.show_menu_screen()
            self.playing = True
            self.reset()  # Reiniciar el estado del juego
         

            while self.playing:
                self.handle_events()
                self.update()
                self.draw()

            if self.bullet_count_enemy > 3:
                self.show_game_over_screen ()
            if self.score > 1000:
                self.show_game_end_screen()

    def handle_events(self):
        event = None  # Inicializar la variable event antes del bucle
        while event is None or event.type != pygame.NOEVENT:  
            event = pygame.event.poll()  

            if event.type == pygame.QUIT:
                if self.playing:
                    self.playing = False
                else:
                    self.running = False

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    if self.playing:
                        self.playing = False
                    else:
                        self.running = False


    def update(self):
        self.spaceship.update()
        self.enemy.update(self.spaceship.rect)
        self.enemy_2.update(self.spaceship.rect)
        self.shield.update(self.spaceship.rect)

        # Verificar colisiones entre las balas del spaceship y el enemigo
        
        collisions = pygame.sprite.spritecollide(self.enemy, self.spaceship.bullets, True)
        if collisions:
            self.enemy.reset_position()
            self.bullet_count += 1
            self.increase_play_score()  # Aumentar el puntaje cuando se golpee a un enemigo

        if not self.shield.is_active():  # Solo verificar colisiones si el escudo no está activo
            # Verificar colisiones entre las balas del Enemy y el spaceship
            collisions = pygame.sprite.spritecollide(self.spaceship, self.enemy.bullets, self.enemy_2.bullets, True)
            if collisions:
                self.bullet_count_enemy += 1
            # collisions = pygame.sprite.spritecollide(self.spaceship, self.enemy_2.bullets, True)
            # if collisions:
            #     self.bullet_count_enemy += 1

        if self.score > 1000 or self.bullet_count_enemy > 4:
            self.playing = False

        self.shield.update(self.spaceship.rect)

        # Verificar colisiones entre las balas del spaceship y el enemigo_2
        
        collisions = pygame.sprite.spritecollide(self.enemy_2, self.spaceship.bullets, True)
        if collisions:
            self.enemy_2.reset_position()
            self.bullet_count += 1
            self.increase_play_score()  # Aumentar el puntaje cuando se golpee a un enemigo

        #if not self.shield.is_active():  # Solo verificar colisiones si el escudo no está activo
            # Verificar colisiones entre las balas del Enemy_2 y el spaceship

        if self.score > 1000 or self.bullet_count_enemy > 4:
            self.playing = False

        # Verificar colisiones entre el spaceship y el shield
        collisions = pygame.sprite.spritecollide(self.shield, self.spaceship.bullets, True)
        if collisions:
            self.shield.deactivate()
            self.shield_active_timer = 30 * FPS  # Configura el tiempo para que el escudo vuelva a aparecer después de 30 segundos
            self.spaceship.activate_immunity()  # Activar inmunidad del spaceship cuando se active el escudo

        # Lógica de Protección contra balas del shield
        if self.shield_active_timer > 0:
            self.shield_active_timer -= 1
            if self.shield_active_timer == 0:
                self.shield.activate()
                #self.spaceship.activate_immunity()  # Activar inmunidad del spaceship cuando se active el escudo
        elif not self.spaceship.is_immune():  # Si el spaceship no está inmunizado
            collisions = pygame.sprite.spritecollide(self.spaceship, self.enemy.bullets, True)
            if collisions:
                self.bullet_count_enemy += 1
            collisions = pygame.sprite.spritecollide(self.spaceship, self.enemy_2.bullets, True)
            if collisions:
                self.bullet_count_enemy += 1



    def draw(self): # lo que se refleja en nuestro Game screen 
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.screen.blit(self.spaceship.image, self.spaceship.rect)
        self.screen.blit(self.enemy.image, self.enemy.rect)
        self.screen.blit(self.enemy_2.image, self.enemy_2.rect)
        self.spaceship.bullets.draw(self.screen)
        self.enemy.bullets.draw(self.screen)
        self.enemy_2.bullets.draw(self.screen)

        # Dibujar el puntaje en la parte superior de la pantalla
        score_text = f"Score: {self.score}"
        score_surface = self.font.render(score_text, True, (255, 255, 255))
        score_rect = score_surface.get_rect()
        score_rect.topleft = (10, 10)
        self.screen.blit(score_surface, score_rect)

        if self.shield.alive:  # Verificar si el escudo está activo
            self.screen.blit(self.shield.image, self.shield.rect)

        # Mostrar el tiempo de inmunidad en la parte superior de la pantalla
        immune_time_text = f"Immune for : {self.spaceship.get_immune_time()}"
        immune_time_surface = self.font.render(immune_time_text, True, (255, 255, 255))
        immune_time_rect = immune_time_surface.get_rect()
        immune_time_rect.topleft = (10, 50)
        self.screen.blit(immune_time_surface, immune_time_rect)

        # Dibujar el número de balas impactadas en el spaceship
        bullet_count_text = f"Inpactos: {self.bullet_count_enemy}"
        bullet_count_surface = self.font.render(bullet_count_text, True, (255, 255, 255))
        bullet_count_rect = bullet_count_surface.get_rect()
        bullet_count_rect.topleft = (10, 100)
        self.screen.blit(bullet_count_surface, bullet_count_rect)
        

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



