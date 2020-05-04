"""
Fonctions.py, on trouvera les fonctions nécessaire
au fonctionnement de la simulations 
"""
import pygame
from random import randrange
import math
from pygame.locals import *


BLACK = (  0,   0,   0)
RED =   (255,   0,   0)


#On crée une liste pour contenir tout les x et y
liste_positions = list()

def position_cercle():
    """
    Fonctions qui donnes les positions initiales
    de chaques cercles
    """
    #Cela permet de générer des nombres aléatoire pour la simulation
    #Ainsi chaque personnes sera placé aleatoirement
    x = randrange(625)
    y = randrange(425)

    liste_positions.append(x)
    liste_positions.append(y)


def nb_cercle():
    """
        Fonction qui crée le nombre d'individu présent 
        dans la simulation
    """
    nombre_individu = input("Entrez le nombre de personnes dans votre simulation (max 200):\n")
    nombre_individu = int(nombre_individu)

    i = 0
    while i < nombre_individu:
        position_cercle()
        i += 1
    return nombre_individu



'''
print("Au début votre liste est vide : ",liste_positions)
compteur = 0
while compteur < 5:
    position_cercle()
    compteur += 1

print("Après appel de la fonctions : ",liste_positions)

print("Parcours de la liste : ")
i = 0
for element in liste_positions:
    print(element)

col = randrange(2)
col = int(col)
print("Nombre aleaotoire : entre 0 et 1 : ",col)

'''