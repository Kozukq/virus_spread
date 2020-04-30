import random

#retourne un booléen généré aléatoirement suivant la probabilité passée en paramètre
def decision(probability):
	return random.random() < probability