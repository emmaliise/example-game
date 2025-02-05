import pygame
from settings import Settings
from player import Player
import game_functions as gf

def run_game():
    pygame.init()
    gm_settings = Settings()

    screen = pygame.display.set_mode([gm_settings.screen_width, gm_settings.screen_height])
    pygame.display.set_caption(gm_settings.caption)
    
    player = Player(screen)

    while True:
        screen.fill(gm_settings.bg_color)
        gf.check_events(player)
        player.update()
        gf.update_screen(gm_settings, screen, player)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                
        player.blit_me()
        pygame.display.flip()
        
    pygame.quit()
    
run_game()