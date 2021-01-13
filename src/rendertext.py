import pygame

class rendertext:
    def __init__(self , text , color , font , size , Surface , loc , bold=False , italic = False):
        self.text = text
        self.font = font
        self.size = size
        self.loc = loc
        self.color = color
        self.Surface = Surface
        self.bold = bold
        self.italic = italic
    def draw(self):
        fonttype = pygame.font.SysFont(self.font , self.size ,self.bold , self.italic)
        act_text = fonttype.render(self.text , False , self.color)
        self.Surface.blit(act_text , self.loc)
