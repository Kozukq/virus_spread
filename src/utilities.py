import random

#retourne un booléen généré aléatoirement suivant la probabilité passée en paramètre
def decision(probability):
	return random.random() < probability

#Liste des noms pouvant être utilisés par la simulation.
namesList = ["Ben", "Gabriel", "Jupiler", "Passepartout", "Bill", "François", "Toumou", "Jacques-Etienne", "Le Montagnard", "Le Pingouin", "Oualoulou", "Chewbacca", "Bubul"]