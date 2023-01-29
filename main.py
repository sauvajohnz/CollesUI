#https://github.com/sauvajohnz
import sys
import pygame
from ui_info import *
from accueil import *
from page_colloscope import *
from bouton_input import *
from page_semaine import *
from bouton_information import *

size = largeur_fenetre, hauteur_fenetre = 1000, 600
version = "0.2"

pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.flip()


ui_gauche = Ui_info(screen, hauteur_fenetre, largeur_fenetre)
ui_gauche.info_version = version
accueil = Page_accueil(screen, hauteur_fenetre, largeur_fenetre)
page_colloscope = Page_colloscope(screen, hauteur_fenetre, largeur_fenetre)
page_semaine = Page_semaine(screen, hauteur_fenetre, largeur_fenetre)


# Boites à input pour l'authentification
input_box_id = InputBox(390, 230, 200, 20)
input_box_pw = InputBox(390, 260, 200, 20, secured=True)
input_boxes = [input_box_id, input_box_pw]
information_box = TextBox(290, 340, 400, 30)
tentative_connexion = 0
phase_authentification = True
guest = False
ui_gauche.info_site = page_colloscope.update_correspondance_colleurmatiere()


def clique(pos):
    x,y = pos[0], pos[1]
    "Determine la position "
    if x < largeur_fenetre // 5.5: #Dans le cas ou on clique sur l'UI:
        if y < ui_gauche.pourcentage_pages*hauteur_fenetre: # Dans le cas ou on change de pages
            if y < ui_gauche.pourcentage_pages*hauteur_fenetre/3: # Page 1
                page_semaine.set_etat(False)
                page_colloscope.set_etat(True)
            elif y < ui_gauche.pourcentage_pages*hauteur_fenetre*2/3: # Page 2
                page_semaine.set_etat(True)
                page_colloscope.set_etat(False)
            else: # Page 3
                print("page3")

#page_colloscope.update_colloscope()

# Skip authentification: (Developer mode only)
skip = False
if skip is True:
    phase_authentification = False
    accueil.etat = False
    ui_gauche.demande_affichage()
    page_colloscope.update_colloscope()
    page_colloscope.set_etat(True)
    page_colloscope.demande_affichage()
    ui_gauche.info_utilisateur = "Sauvajohn"
######

def authentification():
    "Fonction qui s'active quand on demande a s'authentifier"
    global phase_authentification, guest
    autorise = False
    if accueil.verify_id(input_box_id.get_text(), input_box_pw.get_text()) is True:
        autorise = True
        ui_gauche.info_utilisateur = input_box_id.get_text()
    elif ui_gauche.info_site is False:
        ui_gauche.info_utilisateur = "Hors ligne"
        autorise = True
    elif input_box_id.get_text() == "guest":
        autorise = True
        guest = True
        ui_gauche.info_utilisateur = "guest"
    if autorise is True:
        accueil.set_etat(False)
        page_colloscope.set_etat(True)
        ui_gauche.demande_affichage()
        phase_authentification = False
        page_colloscope.update_colloscope()
        page_colloscope.demande_affichage()
    else:
        for box in input_boxes:
            box.set_text('')
            box.draw(screen)

running = True
while running is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONUP:
            clique(pygame.mouse.get_pos())
        elif event.type == pygame.KEYDOWN:
            if phase_authentification is True:
                if event.key == 13: #Entrer
                    tentative_connexion += 1
                    authentification()
        if phase_authentification is True:
            for box in input_boxes:
                box.handle_event(event)


    # Phase d'authentification
    if phase_authentification is True:
        accueil.demande_affichage()
        for box in input_boxes:
            box.draw(screen)
        if tentative_connexion >= 1: # Informe le nombre de tentatives échouées
            information_box.active = True
            information_box.set_text(f"{tentative_connexion} tentative(s) de connexion échouée")
            information_box.draw(screen)
    ##########################
    else:
        ui_gauche.demande_affichage()

    pygame.display.flip()