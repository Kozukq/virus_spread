import pygame
from pygame.locals import *
from fonctions import *
from Personne import *
from random import randrange


WHITE = ( 255, 255, 255)
WIDTH = 640
HEIGHT = 440

class Fenetre:
    def __init__(self):
        self.width = WIDTH
        self.heigth = HEIGHT
        self.window = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.window.fill(WHITE)

def position():
    """
    Fonctions qui donnes les positions initiales
    de chaques cercles
    """
    #Cela permet de générer des nombres aléatoire pour la simulation
    #Ainsi chaque personnes sera placé aleatoirement
    x = randrange(8, 632)
    x = int(x)
    y = randrange(8, 432)
    y = int(y)

    return x,y

"""
Fonction qui génère le 
nombre de personnes souhaitait
"""
def generation_personne(nombre):
    nombre = int(nombre)
    #Création d'une liste de type Personne
    liste_personne = []
    
    i = 0
    if nombre <= 0 or nombre > 200:
        print("Vous avez saisi une valeur inccorecte.")
        exit(1)
    while i < nombre:
        x,y = position()
        liste_personne.append(Personne(d.window, x, y))
        i += 1


d = Fenetre()
generation_personne(50)
#Rafraichissement
pygame.display.flip()


#p = Personne(d.window, 10, 10)



#Boucle qui permet à la fenêtre de rester apparante jusq'ua ce que on clique sur 0
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
	#Rafraichissement
	pygame.display.flip()




