class Behavior:
	def __init__(self, name : str, isCautious : bool, cautionRadius : float,isProtected : bool, movingProb : float):
		#Nom du type de comportement
		self.behaviorName = name
		#Si la personne évite les gens
		self.cautious = isCautious
		#Rayon d'évitement
		if self.cautious:
			self.cautionRadius = cautionRadius

		#Si la personne porte des gants et un masque
		self.protected = isProtected

		#Probabilité de que la personne sorte dehors chaque cycle
		self.movingProb = movingProb


	def displayBehavior(self):
		print("	Behavior : ", self.behaviorName)
		print("	Cautious : ", self.cautious)
		if self.cautious:
			print("	Caution radius : ", self.cautionRadius)		
		print("	Wears protection : ", self.protected)
		print("	Probability of going outside each cycle : ", self.movingProb)


behaviorTypes = {
	"Cautious": Behavior("Cautious", True, 1, True, 0.05),
	"Uncareful": Behavior("Uncareful", False, 0, False, 0.35)
}