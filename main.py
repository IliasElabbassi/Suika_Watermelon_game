import sys, pygame
import pymunk
from Melon import *
from utils import getRgb, nextMelon, static_boundaries
import random
from HUD import HUD
import collision
import val
"""
colors :
Cream                   Coral                   Dusty Rose              Rose Quartz
#F9F1F0 255, 253, 208   #F79489 255, 127, 80    #F8AFA6 220, 174, 150	#FADCD9 247, 202, 201
"""
def main():
    load = (screen, pygame, clock, font, hud) = init()
    hud.main_menu()
    game(load)

def init():
    #game
    pygame.init()
    screen = pygame.display.set_mode((val.width+val.l_width, val.height))
    clock = pygame.time.Clock()
    pygame.font.init() 
    pygame.display.set_caption(val.title)
    font = pygame.font.SysFont('Comic Sans MS', 20)
    #HUD
    hud = HUD(font, pygame, screen) 
    return (screen, pygame, clock, font, hud)
   
def game(load):
    (screen, pygame, clock, font, hud) = load
    #physics
    
    bg_image = pygame.image.load("images\game_bg.png")
    image_rect = bg_image.get_rect()
    image_rect.left, image_rect.top = [0, 0]
    
    space = pymunk.Space()
    space.gravity = (0,500)
    static_boundaries(space, screen, pygame)
    
    melons = []
    next_melon_radius = 10
    next_melon_color = val.all_different_color[val.all_different_radius.index(next_melon_radius)]
    
    #clear all event
    pygame.event.clear(eventtype=None)
    
    while val.game_running:
        events = pygame.event.get()

        for event in events:
            if event.type == pygame.QUIT:
                val.game_running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousse_location_on_click = pygame.mouse.get_pos()
                if mousse_location_on_click[0] >= val.width -25 or mousse_location_on_click[0] <= 25 :
                    continue
                melons.append(Melon(mousse_location_on_click[0], 25, next_melon_radius, getRgb(next_melon_color), space))
                # next melon radius
                (next_melon_radius, next_melon_color) = nextMelon(val.accepted_radius)
        
        # check collision
        collidings = collision.get_melons_colliding(melons)
        (melons, val.accepted_radius) = collision.on_collision(collidings, melons, space, val.accepted_radius)
        
        # draw hud
        screen.blit(bg_image, image_rect)
        #hud.draw(pygame, screen)
        hud.drawNextMelon(next_melon_radius, next_melon_color)
        #mouse_loc = pygame.mouse.get_pos()
        #hud.draw_melon_on_top(next_melon_radius, next_melon_color, mouse_loc[0])
        #static_boundaries(space, screen, pygame)
        
        for melon in melons:
            #melon.update()
            melon.draw(pygame, screen)
        
        space.step(1/50)
        pygame.display.update()
        clock.tick(120)

if __name__ == "__main__":
    import cProfile
    cProfile.run("main()", "output.dat")
    
    import pstats
    from pstats import SortKey
    
    with open("output_time.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("time").print_stats()
        
    with open("output_calls.txt", "w") as f:
        p = pstats.Stats("output.dat", stream=f)
        p.sort_stats("calls").print_stats()

