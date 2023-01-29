import pygame

class InputBox:

    def __init__(self, x, y, w, h, text='', secured=False):
        self.couleur_inactif = (0,0,0)
        self.couleur_actif = (128,128,128)
        self.secured = secured
        self.limite_carac = 17
        self.rect = pygame.Rect(x, y, w, h)
        self.color = self.couleur_inactif
        self.text = text
        self.font = pygame.font.Font(None, 24)
        self.txt_surface = self.font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input_box rect.
            if self.rect.collidepoint(event.pos):
                # Toggle the active variable.
                self.active = True
            else:
                self.active = False
            # Change the current color of the input box.
            self.color = self.couleur_actif if self.active else self.couleur_inactif
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    if len(self.text) < self.limite_carac:
                        self.text += event.unicode
                # Re-render the text.
                self.update()

    def update(self):
        if self.secured is False:
            self.txt_surface = self.font.render(self.text, True, (0, 0, 0))
        else:
            text_etoile = ''
            for _ in range(0, len(self.text)):
                text_etoile += "*"
            self.txt_surface = self.font.render(text_etoile, True, (0, 0, 0))

    def get_text(self):
        return self.text

    def set_text(self, text):
        self.text = text
        self.update()

    def draw(self, screen):
        # Blit the text.
        screen.blit(self.txt_surface, (self.rect.x+2, self.rect.y+2))
        # Blit the rect.
        pygame.draw.rect(screen, self.color, self.rect, 2)

