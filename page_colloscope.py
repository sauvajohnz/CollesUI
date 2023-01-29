import pygame
from infos import *
import json
import requests as rq



class Page_colloscope(pygame.sprite.Sprite):
    def __init__(self, screen, hauteur, largeur):
        super().__init__()
        self.etat = False
        self.font_titre = pygame.font.Font(None, 30)
        self.font_nombre = pygame.font.Font(None, 22)
        self.font = pygame.font.Font(None, 15)
        self.hauteur = hauteur
        self.largeur = largeur
        self.screen = screen
        self.hauteur_case = 30
        self.largeur_case = 30
        self.couleur_fond = (205,255,255)
        self.demande_affichage()

    def demande_affichage(self):
        if self.etat is True:
            self.dessiner()

    def set_etat(self, etat):
        self.etat = etat
        self.demande_affichage()

    def update_correspondance_colleurmatiere(self):
        try:
            demande = f'SELECT * FROM `matiere_colleur`;'
            r = rq.post("https://www.collespsi.fr/demande.php", demande)
            y = json.loads(r.text)
            for dico in y:
                correspondances[dico['nom_colleur']] = dico["matière"]
            for horaire in horaires:
                horaire[0][0] = (correspondances[horaire[0][1][0]],correspondances[horaire[0][1][1]])
            return True
        except:
            return False


    def update_colloscope(self):
        for j in range(0,16):
            y = self.get_db_info_groupecolle( horaires[j][0][1][0], horaires[j][0][2][0].split(" ")[1])
            for dico in y:
                horaires[j][int(dico['semaine']) - 1] = dico['groupe']

    def get_db_info_groupecolle(self, nom_colleur, heure):
        try:
            demande = f'SELECT groupe, semaine FROM `colle` WHERE nom_colleur="{nom_colleur}" and heure="{heure}";'
            r = rq.post("https://www.collespsi.fr/demande.php", demande)
            y = json.loads(r.text)
            if len(y) == 0:
                return " "
            return y
        except:
            return {}

    def dessiner(self):
        #Fond
        pygame.draw.rect(self.screen, self.couleur_fond,
                         pygame.Rect(self.largeur //5.5, 0, self.largeur*(1 - 1/5.5), self.hauteur))

        for j in range(0, 17):
            for i in range(0,17):
                x = 230 + self.largeur // 5.5 + i * self.largeur_case
                y = 30 + j * self.hauteur_case
                if j == 0:
                    y = 20 # Espace de la premiere ligne
                x += (i//5)*10 # Espace toutes les 5 semaines
                pygame.draw.rect(self.screen, (0,0,0),
                                pygame.Rect(x, y, self.largeur_case, self.hauteur_case), 1)
                if j != 0:
                    groupe_colle = horaires[j-1][i+1]
                    if groupe_colle == 0:
                        groupe_colle = "/"
                    self.screen.blit(self.font_nombre.render(str(groupe_colle), True, (0,0,0)),(x+8, y+8))
                else:
                    self.screen.blit(self.font_nombre.render(str(i+1), True, (0,0,0)), (x+8, y+8))


            #Semaine (jour, heure)
            if j != 0:
                for k in range(0,3):
                    self.screen.blit(self.font.render(horaires[j-1][0][k][0], True, (0,0,0)),
                                     (207 + (self.largeur_case*2 - 2)* k, y + 3))
                    self.screen.blit(self.font.render(horaires[j - 1][0][k][1], True, (0, 0, 0)),
                                     (207 + (self.largeur_case*2 - 2) * k, y + self.hauteur_case/2 + 1))
            else:
                self.screen.blit(self.font_titre.render("Semaines", True, (0, 0, 0)),
                                     (255, y + 6))


            pygame.draw.rect(self.screen, (0,0,0),
                            pygame.Rect(205, y, self.largeur_case*6 + 20, self.hauteur_case), 1)


