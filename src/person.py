import pygame

import random
from src.utilities import decision
from src.utilities import namesList
from src.behavior import behaviorTypes
from src.virus import Virus



#Probabilité que la personne aie des problèmes de santé
probHealthIsues = 0.25

#Classe permettant de représenter une personne
class Person:
	def __init__(self, window):
		#Données brutes sur la personne
		self.attributes = {
			"Name": random.choice(namesList),					#Nom de la personne
			"Age": random.randint(10, 99),						#Age de la personne (aléatoire entre 10 et 99)
			"Infected": False,									#Si la personne est infectée
			"Alive": True,										#Si la personne est en vie
			"Cured": False,										#Si la personne est soignée
			"Imminised": False,									#Si la personne est immunisée
			"Comorbidities": decision(probHealthIsues)			#Si la personne à des problèmes de santés existants 
		}
		
		#Comportement de la personne
		self.behavior = behaviorTypes["Cautious"]

		#################################### Graphics part ###################################################
		#TODO : random position entre la hauteur et largeur de la fenêtre
		#Position de la personne dans l'espace
		self.position = pygame.math.Vector2(random.randint(20, window.get_width()-20), random.randint(20,window.get_height()-20))
		self.radius = 15
		self.color = [115, 108, 237]
		self.window = window
		self.width = 1



	#Méthode qui affiche les infos de la personne dans la console
	def displayInfos(self):
		print("Infos : ", self.attributes["Name"])
		print("Position : ", self.position.toString())
		print("Age : ", self.attributes["Age"])
		print("Infected : ", self.attributes["Infected"])
		print("Cured : ", self.attributes["Cured"])
		print("Is immune : ", self.attributes["Imminised"])
		print("Has existing health issues : ", self.attributes["Comorbidities"])
		print("Behavior : ", self.behavior.behaviorName)
		if self.attributes["Infected"]:
			print()
			self.virus.printVirus()

	def draw(self):
		self.rendered = pygame.draw.circle(self.window, self.color, [int(self.position.x), int(self.position.y)], int(self.radius), self.width)

	def move(self, target : pygame.math.Vector2, speed : float):
		if self.position.x != target.x:
			self.position.x += speed/(target.x - self.position.x)
		if self.position.y != target.y:
			self.position.y += speed/(target.y - self.position.y)

	#Méthode lancée chaque cycle par une autre personne lorsqu'elle rentre en contact avec la personne courante.
	#Infecte la personne courante selon la chance d'infection passée en paramètre et avec le virus également passé en paramètre. 
	def infection(self, infectionChance, pathToJson):
		if not self.attributes["Imminised"] and self.attributes["Alive"]:
			if decision(infectionChance):
				self.virus = Virus(self.age, self.healthIssues, pathToJson)
				self.attributes["Infected"] = True

	#Fonction lancée lors de la collision entre 2 personnes
	def collision(self, other):
		if self.attributes["Infected"]:
			#TODO : gérer la réduction du risque de propagation par les masques etc...
			other.infection(self.virus.infectionChance(), self.virus.pathToJson)

def generate(window, n = 100):
	persons = []
	while n > 0:
		persons.append(Person(window))
		n -= 1
	return persons

		


