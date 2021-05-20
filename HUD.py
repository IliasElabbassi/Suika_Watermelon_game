"""
Interface of the game
"""
from utils import getRgb
import pygame
import val
import sys

class HUD:
    def __init__(self, font, pygame, screen):
        self.score = 0
        self.width = val.width
        self.height = val.height
        self.left_HUD_height = val.l_height
        self.left_HUD_width = val.l_width
        self.bg_color = pygame.Color(val.bg_color)
        self.font = font
        self.radius_max = val.all_different_radius[len(val.all_different_radius)-1]
        self.diameter = self.radius_max*2
        self.pygame = pygame
        self.screen = screen
        
    def drawLimitLine(self):
        x = 0
        color = self.pygame.Color((250, 0, 0))
        rect = self.pygame.Rect(x, 50, 10, 10)        
        
        while x < self.width:
            self.pygame.draw.rect(self.screen, color, rect, width=0)
            x = x + 15
            rect = self.pygame.Rect(x, 50, 10, 10)    
    
    def draw(self):
        self.screen.fill(getRgb(self.bg_color))
        #self.drawLimitLine(self.pygame, self.screen)
    
    def drawNextMelon(self, radius, color):
        #self.draw_text("Next Melon", (val.width+val.l_width/3,10), screen)
        p1 = (val.width+50, 50)
        p2 = (self.diameter+2,self.diameter+2)
        #rect = pygame.Rect(p1[0], p1[1], p2[0], p2[1])
        #pygame.draw.rect(screen, (0,0,0), rect, width=1)
        self.pygame.draw.circle(self.screen, getRgb(color), (p1[0]+self.radius_max+4, p1[1]+self.radius_max+1+43), radius-1)
    
    def draw_text(self, text, at):
        textsurface = self.font.render(text, False, (0, 0, 0))
        self.screen.blit(textsurface,(at[0],at[1]))
        
    def draw_melon_on_top(self, radius, color, at_x):
        self.pygame.draw.circle(self.screen, getRgb(color), (at_x, 50), radius-1)
        

    def main_menu(self):
        click = False
        running = True
        while running:
            events = self.pygame.event.get()
            for event in events:
                if event.type == self.pygame.QUIT:
                    running = False
                if event.type == self.pygame.MOUSEBUTTONDOWN:
                    click = True
            
            (mx, my) = mousse_location_on_click = pygame.mouse.get_pos()
        
            
            btn_1 = pygame.Rect((500,400,200,200))
            
            if btn_1.collidepoint(mx, my) and click:
                print("a")
                running = False
                click = False
                
            self.screen.fill((0,130,255))
            self.pygame.draw.rect(self.screen, (100,50,200) , btn_1, width=0)
            self.draw_text("PLAY", (560,475))
            
            self.pygame.display.update()

            
            
            