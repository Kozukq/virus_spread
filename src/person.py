import random
from src.utilities import decision
from src.utilities import namesList
from src.behavior import *
from src.virus import Virus


#Probabilité que la personne aie des problèmes de santé
probHealthIsues = 0.25

#Classe permettant de représenter une personne
class Person:
	def __init__(self):
		self.name = random.choice(namesList)					#Nom de la personne
		self.age = random.randint(10, 99)						#Age de la personne (aléatoire entre 10 et 99)
		self.infected = False									#Si la personne est infectée
		self.alive = True										#Si la personne est en vie
		self.cured = False										#Si la personne est soignée
		self.immunity = False									#Si la personne est immunisée
		self.healthIssues = decision(probHealthIsues)			#Si la personne à des problèmes de santés existants 
		self.behavior = prudent									#Comportement de la personne

	#Méthode qui affiche les infos de la personne dans la console
	def displayInfos(self):
		print("Infos : ", self.name)
		print("Age : ", self.age)
		print("Infected : ", self.infected)
		print("Cured : ", self.cured)
		print("Is immune : ", self.immunity)
		print("Has existing health issues : ", self.healthIssues)
		print("Behavior : ", self.behavior.behaviorName)
		if self.infected:
			print()
			self.virus.printVirus()

	#Méthode lancée chaque cycle par une autre personne lorsqu'elle rentre en contact avec la personne courante.
	#Infecte la personne courante selon la chance d'infection passée en paramètre et avec le virus également passé en paramètre. 
	def infection(self, infectionChance, pathToJson):
		if not self.immunity and self.alive:
			if decision(infectionChance):
				self.virus = Virus(self.age, self.healthIssues, pathToJson)
				self.infected = True

	#Fonction lancée lors de la collision entre 2 personnes
	def collision(self, other):
		if self.infected:
			#TODO : gérer la réduction du risque de propagation par les masques etc...
			other.infection(self.virus.infectionChance(), self.virus.pathToJson)

		


