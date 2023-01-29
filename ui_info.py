import pygame
from datetime import date
import requests as rq

class Ui_info(pygame.sprite.Sprite):
    def __init__(self, screen, hauteur, largeur):
        super().__init__()
        self.etat = True
        self.font = pygame.font.Font(None, 19)
        self.font_titre = pygame.font.Font(None, 24)
        self.pourcentage_info = 0.45  # Pourcentage de l'espace occupé par le compartiment information
        self.pourcentage_pages = 1 - self.pourcentage_info
        self.hauteur = hauteur
        self.largeur = largeur // 5.8
        self.screen = screen
        self.couleur_page1 = (205,255,255)
        self.couleur_page2 = (223, 242, 255)
        self.couleur_page3 = (242, 255, 255)
        self.couleur_boite_info = (116, 208, 241)

        self.info_site = False
        self.info_db = False
        self.info_utilisateur = "1"
        today = date.today()
        self.info_date = today.strftime("%B %d, %Y")
        self.info_version = "0.1"
        self.info_version_disponible = ""


        self.demande_affichage()

    def getmaj(self):
        try:
            r = rq.post("https://www.collespsi.fr/get_collesui_ver.php", "")
            self.info_version_disponible = r.text
        except:
            self.info_version_disponible = "Erreur"

    def compare_maj(self):
        if self.info_version_disponible == "Erreur":
            return "Erreur"
        return "" if self.info_version == self.info_version_disponible else "MAJ Disponible"


    def demande_affichage(self):
        if self.etat is True:
            self.dessiner()

    def connection_site(self):
        return ("On", (0,255,0)) if self.info_site else ("Off", (255,0,0))

    def connection_db(self):
        return ("On", (0,255,0)) if self.info_db else ("Off", (255,0,0))

    def dessiner(self):
        #Page1 (page colloscope)
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
        #Fond
        pygame.draw.rect(self.screen, (0,0,0),
                         pygame.Rect(0, 0, self.largeur, self.hauteur),2)
        #Boite informations
        rect_boite_info = pygame.Rect(0, self.hauteur * self.pourcentage_pages, self.largeur,
                                     self.hauteur * self.pourcentage_info)
        self.screen.fill(self.couleur_boite_info, rect_boite_info)
        pygame.draw.rect(self.screen, (0,0,0), rect_boite_info, 2)

        titres = [("Colloscope", (50, 35)),
                  ("Attribution semaine", (155, 2)),
                  ("Null", (270, 60))
                  ]

        text = [("Utilisateur: ", 10),
                ("Date : ", 60),
                ("Etat de la connexion:", 100),
                ("     Site:", 120),
                ("     Base de donnée:", 140),
                ("Version: ", self.hauteur * self.pourcentage_info - 15)
                ]

        couleur_texte_variable = (255,255,255)
        text_etat = [
            ((self.info_utilisateur, couleur_texte_variable),(10, 80)),
            ((self.info_date, couleur_texte_variable), (60, 45)),
            (self.connection_site(), (120, 140)),
            (self.connection_db(), (140, 140)),
            ((self.info_version, couleur_texte_variable), (self.hauteur * self.pourcentage_info - 15, 60)),
            ((self.compare_maj(), (255,255,0)),  (self.hauteur * self.pourcentage_info - 15, 85))
        ]
        for ligne in titres:
            self.screen.blit(self.font_titre.render(ligne[0], True, (0, 0, 0)),
                            (10 + ligne[1][1], ligne[1][0]))
        for ligne in text:
            self.screen.blit(self.font.render(ligne[0], True, (0, 0, 0)),
                            (5, self.hauteur * self.pourcentage_pages + ligne[1]))
        for ligne in text_etat:
            self.screen.blit(self.font.render(ligne[0][0], True, ligne[0][1]),
                            (ligne[1][1], self.hauteur * self.pourcentage_pages + ligne[1][0]))
