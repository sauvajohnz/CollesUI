import pygame
import hashlib
import json
import requests as rq

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

    def verify_id(self, id, pw):
        try:
            demande = f'SELECT pw FROM `identifiants` WHERE id="{id}"'
            r = rq.post("https://www.collespsi.fr/demande.php", demande)
            if len(r.text) == 0:
                return False
            y = json.loads(r.text)
            pw_b = bytes(pw, 'utf-8')
            if hashlib.sha256(pw_b).hexdigest() == y[0]['pw']:
                return True
            return False
        except:
            return False

    def set_etat(self, etat):
        self.etat = etat
        self.demande_affichage()

    def dessiner(self):
        police = pygame.font.SysFont("monospace", 15)
        message_aide = "Si vous n'avez pas de compte, tapez 'guest' en identifiant"
        pygame.draw.rect(self.screen, self.couleur_fond, pygame.Rect(0, 0, self.largeur, self.hauteur))
        texte_identifiant = police.render("Identifiants",1, (0,0,0))
        texte_guest = police.render(message_aide, 1, (128, 128, 128))
        x_centre_identifiant = texte_identifiant.get_rect(center = self.screen.get_rect().center)[0]
        x_centre_guest = texte_guest.get_rect(center=self.screen.get_rect().center)[0]
        self.screen.blit(texte_identifiant, (x_centre_identifiant, 200))
        self.screen.blit(texte_guest, (x_centre_guest, self.hauteur - 20))




