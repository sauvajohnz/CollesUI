import pygame

class Page_semaine(pygame.sprite.Sprite):
    def __init__(self, screen, hauteur, largeur):
        super().__init__()
        self.etat = False
        self.hauteur = hauteur
        self.largeur = largeur
        self.screen = screen
        self.couleur_fond = (223, 242, 255)
        self.demande_affichage()

    def demande_affichage(self):
        if self.etat is True:
            self.dessiner()

    def set_etat(self, etat):
        self.etat = etat
        self.demande_affichage()

    def dessiner(self):
        #Fond
        pygame.draw.rect(self.screen, self.couleur_fond,
                         pygame.Rect(self.largeur //5.8, 0, self.largeur*(1 - 1/5.8), self.hauteur))