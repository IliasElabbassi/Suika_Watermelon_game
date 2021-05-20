import pygame

title = "Melon Game"
score = 0
size = width, height  = 800, 1000
left_hud_size = l_width, l_height = 400, 1000
game_running = True
bg_color = (255, 253, 208)
all_different_radius = [10,20,30,40,50,70,90,110,130,150]
accepted_radius = [all_different_radius[0]]
all_different_color = [
        pygame.Color((255, 100, 88)),
        pygame.Color((247, 202, 201)),
        pygame.Color((220, 174, 150)),
        pygame.Color((255, 127, 80)),
        pygame.Color((255, 0, 0)),
        pygame.Color((0, 255, 0)),
        pygame.Color((0, 0, 255)),
        pygame.Color((50, 50, 255)),
        pygame.Color((255, 0, 255)),
        pygame.Color((255, 255, 0))
        ]