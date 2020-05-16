import pygame

import random
import time
import random
from src.behavior import behaviorTypes
from src.virus import Virus

def decision(probability):
	return random.random() < probability

namesList = ["Ben", "Gabriel", "Jupiler", "Passepartout", "Bill", "François", "Toumou", "Jacques-Etienne", "Le Montagnard", "Le Pingouin", "Oualoulou", "Chewbacca", "Bubul"]		

diseases = []

#Probabilité que la personne aie des problèmes de santé
probHealthIsues = 0.25



#Classe permettant de représenter une personne
class Person:
	def __init__(self, window):
		#Données brutes sur la personne
		self.name = random.choice(namesList)
		self.age = random.randint(10,99)
		self.isAlive = True
		self.isInfected = False
		self.isCured = False
		self.isImmune = False
		#healthIssues = []
		
		#Comportement de la personne
		self.behavior = behaviorTypes["Cautious"]

		#################################### Graphics part ###################################################
		#Position de la personne dans l'espace
		self.position = pygame.math.Vector2(random.randint(20, window.get_width()-20), random.randint(20,window.get_height()-20))
		self.radius = 7
		self.color = [115, 108, 237]
		self.window = window
		self.width = 0
		#Vecteur normalisé représentant la direction
		self.direction = pygame.math.Vector2(random.uniform(-1,1), random.uniform(-1, 1)).normalize()
		self.hitbox = pygame.Rect((self.position.x)-5, (self.position.y)-5, self.radius*1.3, self.radius*1.3)
		self.speed = 30
		self.isMoving = True

	#Méthode qui affiche les infos de la personne dans la console
	def debug(self):
		print("Infos : ", self.name)
		print("Position : ", self.position.toString())
		print("Age : ", self.age)
		print("Infected : ", self.isInfected)
		print("Cured : ", self.isCured)
		print("Is immune : ", self.isImmune)
		#print("Has existing health issues : ", self.attributes["Comorbidities"])
		print("Behavior : ", self.behavior.behaviorName)
		if self.isInfected:
			print()
			self.virus.debug()

	########Graphics########

	def draw(self):
		pygame.draw.circle(self.window, self.color, [int(self.position.x), int(self.position.y)], int(self.radius), self.width)
		# pygame.draw.rect(self.window, [0,0,0], self.hitbox,1)

	def moveTowards(self, target : pygame.math.Vector2, speed : float):
		self.position += (target - self.position).normalize() * speed

	def bounce(self, vert):
		if vert:
			self.direction.x = -self.direction.x
		else:
			self.direction.y = -self.direction.y

	def move(self, deltaTime):
		if self.isMoving:
			self.position += self.direction * self.speed / deltaTime
			self.hitbox.center = (self.position.x, self.position.y)
			if self.position.x >= self.window.get_width() or self.position.x <= 0:
				self.bounce(True)
			if self.position.y >= self.window.get_height() or self.position.y <= 0:
				self.bounce(False)


	def checkForCollisions(self, list, persons):
		list2 = list[:]
		list2.remove(self.hitbox)
		
		index = self.hitbox.collidelist(list2)
		if index > -1:
			if self.hitbox.center[0] - self.hitbox.left < list2[index].center[0]+list2[index].right or self.hitbox.center[0] + self.hitbox.right > list2[index].center[0]-list2[index].left:
				self.bounce(True)
			if self.hitbox.center[1] - self.hitbox.top < list2[index].center[1]+list2[index].bottom or self.hitbox.center[1] + self.hitbox.bottom > list2[index].center[1]-list2[index].top:
				self.bounce(False)
			if persons[index].isInfected:
				self.infection(1, "Virus Presets/Covid.json")

	#Fonction lancée lors de la collision entre 2 personnes
	def collision(self, other):
		if self.isInfected:
			#TODO : gérer la réduction du risque de propagation par les masques etc...
			other.infection(self.virus.infectionChance(), self.virus.pathToJson)

	########Infection########

	#Méthode lancée chaque cycle par une autre personne lorsqu'elle rentre en contact avec la personne courante.
	#Infecte la personne courante selon la chance d'infection passée en paramètre et avec le virus également passé en paramètre. 
	def infection(self, infectionChance, pathToJson):
		if (not self.isImmune) and self.isAlive:
			if decision(infectionChance):
				self.virus = Virus(self.age,False, pathToJson)
				self.isInfected = True
				#self.color = [255,0,0]
				self.infectionTime = time.time()

	def personUpdate(self):
		if self.isInfected:
			if time.time()-self.infectionTime >= self.virus.deathChance:
				self.isAlive = False
			else:
				self.isCured = True
		self.updateColor()

	def updateColor(self):
		if self.isAlive:
			if self.isImmune:
				self.color = [0,0,255]
			elif self.isInfected:
				self.color = [255,0,0]
			elif self.isCured:
				self.color = [0,255,0]
		else:
			self.color = [0,0,0]
			self.isMoving = False

def generate(window, n = 100):
	persons = []
	while n > 0:
		persons.append(Person(window))
		n -= 1
	hitboxes = []
	for person in persons:
		hitboxes.append(person.hitbox)
	return persons, hitboxes

