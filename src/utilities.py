import random

#retourne un booléen généré aléatoirement suivant la probabilité passée en paramètre
def decision(probability):
	return random.random() < probability

#Liste des noms pouvant être utilisés par la simulation.
namesList = ["Ben", "Gabriel", "Jupiler", "Passepartout", "Bill", "François", "Toumou", "Jacques-Etienne", "Le Montagnard", "Le Pingouin", "Oualoulou", "Chewbacca", "Bubul"]

#Classe permettant de modéliser des vecteurs 2D.
class Vector2D:
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def toString(self):
		return "["+str(self.x)+","+str(self.y)+"]"