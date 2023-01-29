import pygame

class Page_accueil(pygame.sprite.Sprite):
    def __init__(self, screen, hauteur, largeur):
        super().__init__()
        self.etat = True
        self.hauteur = hauteur
        self.largeur = largeur
        self.screen = screen
        self.couleur_fond = (205,255,255)

        self.demande_affichage()

    def demande_affichage(self):
        if self.etat is True:
            self.dessiner()

    def set_etat(self, etat):
        self.etat = etat
        self.demande_affichage()

    def dessiner(self):
        police = pygame.font.SysFont("monospace", 15)
        #Fond
        pygame.draw.rect(self.screen, self.couleur_fond, pygame.Rect(0, 0, self.largeur, self.hauteur))

        texte_identifiant = police.render("Identifiants",1, (0,0,0))
        self.screen.blit(texte_identifiant, (435,200))




