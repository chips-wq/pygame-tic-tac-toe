import pygame
class buton:
    def __init__(self , rect , color , text = ''):
        self.rect = rect
        self.color = color
        self.text = text
    def draw(self , Surface , functie):
        pygame.draw.rect(Surface , self.color , self.rect)
        if not (self.text == ''):
            fonttype = pygame.font.SysFont('Arial' , 20)
            textsurface = fonttype.render(self.text , False , (0,0,0))
            Surface.blit(textsurface , (self.rect[0] + 10 , self.rect[1] + 5))
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    if event.pos[0] > self.rect[0] and event.pos[0] < self.rect[0]+self.rect[2] and event.pos[1] > self.rect[1] and event.pos[1] < self.rect[1] + self.rect[3]:
                        return functie()
            if event.type == pygame.QUIT:
                exit()
