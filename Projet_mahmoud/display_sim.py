import pygame
import Fonctions
from Fonctions import *
from pygame.locals import *
from random import randrange

#Initialisation des modules pygame
pygame.init()

pose_x = 0
pose_y = 0

alea = randrange(50)
print(alea)
WHITE = (255, 255, 255)
BLACK = (  0,   0,   0)
RED =   (255,   0,   0)
couleur = 1

#Déclaration d'une fenêtre 
fenetre = pygame.display.set_mode((640, 440), RESIZABLE)
fenetre.fill(WHITE)
#importation d'une image


nb = nb_cercle()
print("Il y a {} personnes dans la simulation.".format(nb))
print(liste_positions)

i = 0
j = 1
while i < nb and j <= nb:
	
	pygame.draw.ellipse(fenetre, BLACK, [liste_positions[i], liste_positions[j], 15, 15], couleur) 
	i += 1
	j += 1


#Raffrichissement de l'écran
pygame.display.flip()

#Boucle qui permet à la fenêtre de rester apparante jusq'ua ce que on clique sur 0
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
   
	#Rafraichissement
	pygame.display.flip()




