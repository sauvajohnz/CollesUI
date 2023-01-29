import pygame

class Ui_info(pygame.sprite.Sprite):
    def __init__(self, screen, hauteur, largeur):
        super().__init__()
        self.etat = True
        self.pourcentage_info = 0.45  # Pourcentage de l'espace occupé par le compartiment information
        self.pourcentage_pages = 1 - self.pourcentage_info
        self.hauteur = hauteur
        self.largeur = largeur // 5.5
        self.screen = screen
        self.couleur_page1 = (0, 0, 100)
        self.couleur_page2 = (0, 0, 160)
        self.couleur_page3 = (0, 0, 210)
        self.couleur_boite_info = (255, 25, 255)

        self.connection_site = False
        self.connection_db = False
        self.text = "Utilisateur: \nDate:\nConnexion site:\nConnexion base donnnée:\nVersion:"

        self.demande_affichage()

    def demande_affichage(self):
        if self.etat is True:
            self.dessiner()

    def dessiner(self):
        #Page1
        pygame.draw.rect(self.screen, self.couleur_page1,
                         pygame.Rect(0, 0, self.largeur, self.hauteur * self.pourcentage_pages*1/3))
        #Page2
        pygame.draw.rect(self.screen, self.couleur_page2,
                         pygame.Rect(0, self.hauteur * (self.pourcentage_pages * 1 / 3), self.largeur,
                                     self.hauteur * self.pourcentage_pages*1/3))
        #Page3
        pygame.draw.rect(self.screen, self.couleur_page3,
                         pygame.Rect(0, self.hauteur * (self.pourcentage_pages * 2 / 3), self.largeur,
                                     self.hauteur * self.pourcentage_pages * 1 / 3))
        #Boite informations
        pygame.draw.rect(self.screen, self.couleur_boite_info,
                         pygame.Rect(0, self.hauteur * self.pourcentage_pages, self.largeur,
                                     self.hauteur * self.pourcentage_info))
