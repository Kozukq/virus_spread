from random import randrange, randint
from random import choice

from CONSTANTES import *

def choice_prenom():
    """
        Fonction qui choisi un prénom de façon aléatoire
    """
    number = randrange(1, 17)
    number = str(number)
    return number

def get_comorbidity():
    """
        Fonction qui détermine la comorbidité 
        d'une personne de manière aléatoire 
    """
    number = randint(1,3)
    number = int(number)

    if number == 1:
        risque = "PEU-A-RISQUE"
        return risque
    if number == 2:
        risque = "RISQUE-MODEREE"
        return risque
    if number == 3:
        risque = "RISQUE-HAUT"
        return risque

        

def age_alea():
    """
    Fonction qui retourne un âge de manière aléatoire
    """
    age = randrange(2, 90)
    age = int(age)
    return age


def afficher(*parametres, sep='', fin='\n'):
    #On converti les tuples de la liste en liste
    parametres = list(parametres)
    for i, parametre in enumerate(parametres):
        parametres[i] = str(parametre)
    chaine = sep.join(parametres)
    # On ajoute le paramètre fin à la fin de la chaîne
    chaine += fin
    # On affiche l'ensemble
    print(chaine, end='')
    