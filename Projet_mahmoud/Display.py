import pygame
from pygame.locals import *

#importation des fichiers de la simulation
from Class import *
from fonctions import *
from CONSTANTES import *


liste_personne = []
def generation_personne(nombre):
    """
    Fonction qui génère le 
    nombre de personnes souhaitait
    """
    nombre = int(nombre)
    #Création d'une liste de type Personne
    
    i = 0
    if nombre <= 0 or nombre > 200:
        print("Vous avez saisi une valeur inccorecte.")
        exit(1)
    while i < nombre:
        x,y = position()
        liste_personne.append(Personne(d.window, x, y))
        i += 1
    

#Instantiation de la class Fenêtre
d = Fenetre()

#Saisi du nombre de personnes dans la simulation
nombre = input("Entrez le nombre de personnes présente dans la simulation : ")
try:
    nombre = int(nombre)
    assert nombre > 0
except ValueError as type_exception:
    print("Vous avez saisi autre chose que un nombre.")
    exit(1)
except AssertionError:
    print("Le nombre saisi est < 0!!")
    exit(1)

generation_personne(nombre)#On appel la fonction generation pour crée les personnes
             
                


taille = len(liste_personne)
print("Il y a {} personne(s) dans la simulation.\n".format(taille))

#On affiche dans la console les personnes présentent dans la simulation
afficher(liste_personne)

"""
Pour acceder à un attribut :
age = liste_personne[0]._get_age()
print("L'age : ",age)
"""

#Boucle qui permet à la fenêtre de rester apparante jusq'ua ce que on clique sur 0
continuer = 1
while continuer:
	for event in pygame.event.get():	#Attente des événements
		if event.type == QUIT:
			continuer = 0
        
	#Rafraichissement
	pygame.display.flip()





