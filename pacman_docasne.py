import pygame # klíčová knihovna umožňující vytvářet jednoduše nejen hry
pygame.init()

class Cross(pygame.sprite.Sprite):
    def __init__(self,xpos, ypos): # konstruktor - volá se vždy při vytvoření (inicializaci)
        super().__init__()
        self.surface = pygame.Surface((1,1))
        self.surface.fill("white")
        self.xpos = xpos
        self.ypos = ypos
        #screen.blit(self,(self.xpos,self.ypos))
    
    def update(self):
        


cross1 = Cross(25,25)


window_width = 800
window_height = 400
screen = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() # zavřeme herní okno
            exit()
    
    cross1.draw(screen)
    cross1.update()
    
    pygame.display.update() # updatujeme vykreslené okno
    clock.tick(60)