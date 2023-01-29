import pygame

class Bouton:
    def __init__(self, x, y, w, h, text=''):
        self.largeur = w
        self.x = x
        self.couleur_inactif = (255,255,255)
        self.couleur_actif = (128,128,128)
        self.limite_carac = 17
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.couleur_inactif
        self.text = text
        self.font = pygame.font.Font(None, 24)
        self.txt_surface = self.font.render(text, True, (0,0,0))
        self.active = True

    def activation(self):
        print("On m'a appuyé dessus")

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                if self.active:
                    self.activation()
            # Change the current color of the input box.
            #self.color = self.couleur_actif if self.active else self.couleur_inactif


    def draw(self, screen):
        # Blit the text.
        screen.fill(self.color, self.rect)
        x_centre = self.txt_surface.get_rect(center = (self.x + self.largeur/2,0))[0]
        # Blit the rect.
        pygame.draw.rect(screen, (0,0,0), self.rect, 2)
        screen.blit(self.txt_surface, (x_centre, self.rect.y + 7))

