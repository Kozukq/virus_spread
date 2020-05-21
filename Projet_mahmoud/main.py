import pygame
from pygame.locals import *

import sys
from math import *
from random import *

#Fichiers sources
from fonctions import *
from CONSTANTES import *


"""
    Saisi des paramètres de la simulation
"""
print("********************************************************\n")
print("****Utiliser la surface par défaut (640 x 440) (o/n)****\n")
print("********************************************************\n")
choix = input("                           ")
choix = str(choix)
if choix.capitalize() == "O":
    WIDTH = 640
    HEIGHT = 440
elif choix.capitalize() == "N":
    print("\n\nVous avez choisez de crée votre propre surface : ")
    WIDTH = input("WIDTH (640 < X < 1280) : ")
    HEIGHT = input("HEIGHT (440 < X < 880) : ")

print("\n\n**********IDICATION DES COULEURS**********\n")
print("=====VERT : personne non malade")
print("=====JAUNE : personne non malade confiné")
print("=====ROUGE : personne malade")
print("=====BLEU : personne non malade contaminé au cour de la simulation")
print("=====ORANGE : personne malade confiné")
print("=====NOIR : personne décidé")

print("\n**********PARAMETRES DE LA SIMULATION**********")
nombre_P_N_Malade = input("\n**Entrez le nombre de personnes non malade (VERT): ")
nombre_P_N_M_Confinee = input("**Entrez le nombre de personnes non malade confinée (JAUNE): ")
nombre_P_Infectee = input("**Entrez le nombre de personnes malade (ROUGE): ")
nombre_P_I_Confinee = input("**Entrez le nombre de personnes malade confinée (ORANGE): ")
vitesse = input("**Choisissez la vitesse de déplacement des personnes (1-2-3) : ")

try:
    nombre_P_N_Malade = int(nombre_P_N_Malade)
    nombre_P_N_M_Confinee = int(nombre_P_N_M_Confinee)
    nombre_P_Infectee = int(nombre_P_Infectee)
    nombre_P_I_Confinee = int(nombre_P_I_Confinee)
    vitesse = int(vitesse)
    WIDTH = int(WIDTH)
    HEIGHT = int(HEIGHT)

    assert nombre_P_N_Malade > 0
    assert nombre_P_N_M_Confinee > -1
    assert nombre_P_Infectee > -1
    assert nombre_P_I_Confinee > -1
    assert vitesse > 0
    assert WIDTH > 639
    assert WIDTH > 439

except ValueError as type_exception:
    print("Vous avez saisi autre chose que un nombre dans l'un des champs.")
    exit(1)
except AssertionError:
    print("L'un des nombre saisi est pas convenable!!")
    exit(1)

nbT = nombre_P_N_Malade + nombre_P_N_M_Confinee + nombre_P_Infectee + nombre_P_I_Confinee 

if nbT > 200:
    print("\n         **********************************")
    print("Vous avez dépassez la limite maximal de personnes (200)!!")
    print("         **********************************\n")
    exit(1)
elif vitesse > 3:
    print("\n         **********************************")
    print("       Vous avez saisez une vitesse incorecte!!")
    print("         **********************************\n")
    exit(1)
elif WIDTH > 1280 or HEIGHT > 880:
    print("\n       **********************************\n")
    print("Vous avez saisez une résolution de la surface supérieur à la limite autorisé!!")
    print("         **********************************\n")
    exit(1)
elif nbT > 150 and vitesse < 3:
    print("\n                 **********************************")
    print("     Vous avez demandez un trop grand nombre de personnes ({})\n      vous devez choisirs la vitesse 3 au lieu de {} réessayez.".format(nbT, vitesse))
    print("                 **********************************\n")
    exit(1)
else:
    if vitesse == 1:
        v = 0.05
    elif vitesse == 2:
        v = 0.1
    elif vitesse == 3:
        v = 0.6

pygame.init()

pygame.display.set_caption("COVID-19 ({}, {})".format(WIDTH, HEIGHT))
Surface = pygame.display.set_mode((WIDTH, HEIGHT))
#Liste de circles
Personnes = []


#Class Circle
class Circle:
    """
        Class Circle, possèdant deux paramètres : 
            > couleur (GOOD/ BAD/ IMMUNE/ DEAD )
            > vie ( VIVANT/ MORT)
        Attributs : 
            >radius le diamètre d'un cercle
            >prénom, âge, comorbidité
            >position initial (x, y)
            >la vitesse de déplacement d'un cercle trois niveaux (1-2-3)
    """
    def __init__(self, couleur, vie, v):
        self.radius = 8#Le diametre d'un cercle
        self.prenom = dico_prenom[choice_prenom()]
        self.age = age_alea()
        self.comorbidity = get_comorbidity()
        self.etat = ETAT[vie]
        self.color = COLOR[couleur]
        self.pos_x = randint(self.radius, WIDTH - self.radius)#La position x aleatoire du début
        self.pos_y = randint(self.radius, HEIGHT - self.radius)#La position y aleatoire du début
        self.speedx = v * (random() + 1.0)#Renvoie le prochain nombre à virgule flottante aléatoire dans la plage [0,0, 1,0].
        self.speedy = v * (random() + 1.0)
 

    def __repr__(self):
        """
            Fonction spécial qui se charge de la représentation d'une personne
        """
        return "\nPrénom :                       {}\n   Age :                       {}ans,\nComorbidité :                  {}\nEtat :                         {}".format(
                self.prenom, self.age, self.comorbidity, self.etat)

def affichage_Resume():
    print("\n\n*********RESUME*********\n\nIndividu non malade : {}\nIndividu confinée non malade : {}\nIndividu malade : {}\nIndividu confinée malade : {}".format(nombre_P_N_Malade,nombre_P_N_M_Confinee, nombre_P_Infectee,nombre_P_I_Confinee))


def Draw():
    """
        Fonction qui crée les cercles
    """
    Surface.fill(WHITE)
    for circle in Personnes:
        pygame.draw.circle(Surface, circle.color, (int(circle.pos_x), int(circle.pos_y)), circle.radius)
    pygame.display.flip()


def Move():
    """
        Fonction qui permet de bouger les cercles
    """
    for element in Personnes:
        element.pos_x += element.speedx
        element.pos_y += element.speedy


def Collision(C1,C2):
    """
        Fonction qui gère les trajéctoires lors des collisions
        On crée une variable pour garder la vitesse initial lors des collisions
        On défini la différence entre les points x et y de chaque cercles
        On crée un angle pour chaque situation XDiff < 0 > 0 == 0 idem pour YDiff
        On assigne a la vitesse de chaque pos X et Y grâce a la trigo cos et sin et tan
    """
    C1Speed = sqrt((C1.speedx**2) + (C1.speedy**2))#Sert a garder la même vitesse après collision
    XDiff = -(C1.pos_x - C2.pos_x)
    YDiff = -(C1.pos_y - C2.pos_y)

    if XDiff > 0:#On teste Si la diff entre deux pos_x > 0

        #Si diff entre les y de deux cercles est > 0
        if YDiff > 0:#Les deux points sont dans la surface
            Angle = degrees(atan(XDiff / YDiff))#On crée un angle de trajéctoire en degrés en utilisant tan(diff entre Y / diff entre X)
            XSpeed = -C1Speed * cos(radians(Angle))#On affecte a XPeed C1Speed(on garde la vitesse de base) * cos(l'angle crée)
            YSpeed = -C1Speed * sin(radians(Angle))

        elif YDiff < 0:#Les deux points sont au murs de la surface
            Angle = degrees(atan(XDiff / YDiff))
            XSpeed = -C1Speed * cos(radians(Angle))
            YSpeed = -C1Speed * sin(radians(Angle))

    elif XDiff < 0:
        if YDiff > 0:
            Angle = 180 + degrees(atan(XDiff / YDiff))
            XSpeed = -C1Speed * cos(radians(Angle))
            YSpeed = -C1Speed * sin(radians(Angle))

        elif YDiff < 0:
            Angle = -180 + degrees(atan(XDiff/YDiff))
            XSpeed = -C1Speed * cos(radians(Angle))
            YSpeed = -C1Speed * sin(radians(Angle))
            
    elif XDiff == 0:
        if YDiff > 0:
            Angle = -90
        else:
            Angle = 90

        XSpeed = C1Speed * cos(radians(Angle))
        YSpeed = C1Speed * sin(radians(Angle))

    elif YDiff == 0:
        if XDiff < 0:
            Angle = 0
        else:
            Angle = 180

        XSpeed = C1Speed * cos(radians(Angle))
        YSpeed = C1Speed * sin(radians(Angle))
        
    C1.speedx = XSpeed
    C1.speedy = YSpeed


def Collision_Detect():
    """
        Fonction qui permet de détécté une sortie de surface 
        et ainsi faire rebondir le cercle dans le sens opposé

        Et gère la collision entre deux cercles
    """
    #Boucle qui détérmine la collision d'un cercle au bord de la fenêtre
    for circle in Personnes:
        if circle.pos_x < circle.radius or circle.pos_x > WIDTH - circle.radius:#Gère la collision a droite et à gauche de la surface
            circle.speedx *= -1
        if circle.pos_y < circle.radius or circle.pos_y > HEIGHT - circle.radius:#Gère la collision en haut et en bas de la surface    
            circle.speedy *= -1
            
    #Boucle qui détérmine la collision entre deux cercles
    for c1 in Personnes:
        for c2 in Personnes:
            if c1 != c2:
                if sqrt( ((c1.pos_x - c2.pos_x) ** 2)  +  ((c1.pos_y - c2.pos_y) ** 2)) <= (c1.radius + c2.radius):
                    Collision(c1, c2)
                    #testes de contaminations
                    if c1.color == COLOR["COLOR_GOOD"] and c2.color == COLOR["COLOR_BAD"] or c1.color == COLOR["COLOR_GOOD"] and c2.color == COLOR["COLOR_CONTAMINEE"]:
                        c1.color = COLOR["COLOR_CONTAMINEE"]
                    if c1.color == COLOR["COLOR_GOOD_CONF"] and c2.color == COLOR["COLOR_BAD"]:
                        c1.color == COLOR["COLOR_GOOD_CONF"]
                    if c1.color == COLOR["COLOR_BAD_CONF"] and c2.color == COLOR["COLOR_BAD"] or c1.color == COLOR["COLOR_BAD_CONF"] and c2.color == COLOR["COLOR_GOOD"]:
                        c1.color == COLOR["COLOR_BAD_CONF"]
                    if c1.color == COLOR["COLOR_CONTAMINEE"] and c1.comorbidity == "RISQUE-HAUT":
                        c1.color = COLOR["COLOR_DEAD"]
                        c1.speedx = 0
                        c1.speedy = 0
                    if c2.color == COLOR["COLOR_CONTAMINEE"] and c2.comorbidity == "RISQUE-HAUT":
                        c2.color = COLOR["COLOR_DEAD"]
                        c2.speedx = 0
                        c2.speedy = 0


def EXIT():
    quitter = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or quitter[K_ESCAPE]:
            print("AU REVOIR")
            pygame.quit(); sys.exit()
        


#Boucle qui ajoute les cercles correspondant dans la liste Personnes
for i in range(nombre_P_N_Malade):
    vie = "VIVANT"
    normal = "COLOR_GOOD"
    normal = str(normal)
    Personnes.append(Circle(normal, vie, v))

for j in range(nombre_P_Infectee):
    vie = "VIVANT"
    malade = "COLOR_BAD"
    malade = str(malade)
    Personnes.append(Circle(malade, vie, v))

for i in range(nombre_P_N_M_Confinee):
    vie = "VIVANT"
    normal = "COLOR_GOOD_CONF"
    v = 0
    normal = str(normal)
    Personnes.append(Circle(normal, vie, v))

for j in range(nombre_P_I_Confinee):
    vie = "VIVANT"
    malade = "COLOR_BAD_CONF"
    malade = str(malade)
    v = 0
    Personnes.append(Circle(malade, vie, v))




#On affiche dans la console les personnes présentent dans la simulation
afficher(Personnes)
affichage_Resume()

#Rappel des indication de couleurs
print("\n\n**********IDICATION DES COULEURS**********\n")
print("=====VERT : personne non malade")
print("=====JAUNE : personne non malade confiné")
print("=====ROUGE : personne malade")
print("=====BLEU : personne non malade contaminé au cour de la simulation")
print("=====ORANGE : personne malade confiné")
print("=====NOIR : personne décidé")


def main():
    while True:
        EXIT()
        Move()
        Collision_Detect()
        Draw()
if __name__ == '__main__': main()
