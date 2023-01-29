import pygame

class TextBox:

    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.largeur = w
        self.color = (0,0,0)
        self.text = text
        self.font = pygame.font.Font(None, 22)
        self.txt_surface = self.font.render(self.text, True, (0,0,0))
        self.active = False

    def set_text(self, text):
        self.text = text
        self.txt_surface = self.font.render(self.text, True, (0, 0, 0))

    def draw(self, screen):
        if self.active is True:
            # Blit the text.)
            screen.fill((255,0,0), self.rect)
            screen.blit(self.txt_surface, (self.rect.x + self.largeur/2 - 4.2*len(self.text), self.rect.y +8))
            # Blit the rect.
            pygame.draw.rect(screen, self.color, self.rect, 1)

