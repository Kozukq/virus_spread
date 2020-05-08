import pygame
from pygame.locals import *
from CONSTANTES import *
from fonctions import *

"""
Class fenetre
"""
class Fenetre:
    def __init__(self):
        self.width = WIDTH
        self.heigth = HEIGHT
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.window.fill(WHITE)
       

"""
Class Personne
"""
class Personne:
    def __init__(self, fenetre, pos_x, pos_y):
        self.window = fenetre
        self.prenom = dico_prenom[choice_prenom()]
        self.age = age_alea()
        self.comorbidity = get_comorbidity()
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.circle = pygame.draw.circle(self.window, COLOR["COLOR_GOOD"], [pos_x, pos_y], 9, 0)
    
    def __repr__(self):
        """
            Fonction spécial qui ce charge de l'affichage d'une personne
        """
        return "\nPrénom :                       {}\n   Age :                       {}ans,\nComorbidité :                  {}\nPosition dans la simulation :  ({},{})\n".format(
                self.prenom, self.age,self.comorbidity, self.pos_x, self.pos_y)
    
    def _get_position(self):
        """
            Fonction qui retourne la position courante d'une personne
        """
        return self.pos_x, self.pos_y
    
    def _get_age(self):
        """
            Fonction qui retourne l'âge d'une personne
        """
        return self.age
    
    def _set_position(self, nv_pos_x, nv_pos_y):
        """
            Fonction qui modifie la position d'une personne
        """
        self.pos_x = nv_pos_x
        self.pos_y = nv_pos_y
    
