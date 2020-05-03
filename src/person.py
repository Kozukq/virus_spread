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
		#Position de la personne dans l'espace
		self.position = pygame.math.Vector2(random.randint(20, window.get_width()-20), random.randint(20,window.get_height()-20))
		self.radius = 5
		self.color = [115, 108, 237]
		self.window = window
		self.width = 1
		#Vecteur normalisé représentant la direction
		self.direction = pygame.math.Vector2(random.uniform(-1,1), random.uniform(-1, 1)).normalize()
		self.hitbox = pygame.Rect((self.position.x)-5, (self.position.y)-5, 10, 10)



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

	def moveTowards(self, target : pygame.math.Vector2, speed : float):
		self.position += (target - self.position).normalize() * speed

	def bounce(self, vert):
		if vert:
			self.direction.x = -self.direction.x
		else:
			self.direction.y = -self.direction.y

	def move(self, speed):
		self.position += self.direction * speed
		if self.position.x <= 0:
			self.bounce(True)
		if self.position.x >= self.window.get_width():
			self.bounce(True)
		if self.position.y <= 0:
			self.bounce(False)
		if self.position.y >= self.window.get_height():
			self.bounce(False)




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

		


