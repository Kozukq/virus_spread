import pygame

import random
import time
import random
from src.behavior import behaviorTypes
from src.virus import Virus

def determineFrom(probability):
	return random.random() < probability

namesList = ["Ben", "Gabriel", "Jupiler", "Passepartout", "Bill", "François", "Toumou", "Jacques-Etienne", "Le Montagnard", "Le Pingouin", "Oualoulou", "Chewbacca", "Bubul"]		

#diseases = []

#Probabilité que la personne aie des problèmes de santé
sicknessRate = 0.25


#Classe permettant de représenter une personne
class Person:
	def __init__(self, Rect):
		#Données brutes sur la personne
		self.name = random.choice(namesList)
		self.age = random.randint(10,99)
		self.isAlive = True
		self.isInfected = False
		self.isCured = False
		self.healthIssues = determineFrom(sicknessRate)
		self.equipment = { "mask" : False }

		#Comportement de la personne
		self.behavior = behaviorTypes["Cautious"]

		#################################### Graphics part ###################################################
		#Position de la personne dans l'espace
		self.rect = Rect
		self.position = pygame.math.Vector2(random.randint(self.rect.left+20, self.rect.right-20), random.randint(self.rect.top+20,self.rect.bottom-20))
		self.radius = 7
		self.color = [115, 108, 237]
		self.width = 0
		self.timestamp = None
		#Vecteur normalisé représentant la direction
		self.direction = pygame.math.Vector2(random.uniform(-1,1), random.uniform(-1, 1)).normalize()
		self.hitbox = pygame.Rect((self.position.x)-5, (self.position.y)-5, self.radius*1.3, self.radius*1.3)
		self.speed = 20
		self.isMoving = True

		self.virus = None
		self.infectionTime = None
		self.willDie = None


	#Méthode qui affiche les infos de la personne dans la console
	def debug(self):
		print("Infos : ", self.name)
		print("Position : ", self.position.toString())
		print("Age : ", self.age)
		print("Infected : ", self.isInfected)
		print("Cured : ", self.isCured)
		print("Has health issues : ", self.healthIssues)
		print("Behavior : ", self.behavior.behaviorName)
		if self.isInfected:
			print()
			self.virus.debug()

	########Graphics########

	def draw(self, Window):
		pygame.draw.circle(Window, self.color, [int(self.position.x), int(self.position.y)], int(self.radius), self.width)
		pygame.draw.rect(Window, [0,0,0], self.hitbox,1)

	def moveTowards(self, target : pygame.math.Vector2, speed : float):
		self.position += (target - self.position).normalize() * speed

	# def bounce(self, vert):
	# 	if not self.timestamp:
	# 		self.timestamp = time.time()
	# 		if vert:
	# 			self.direction.x = -self.direction.x
	# 		else:
	# 			self.direction.y = -self.direction.y
	# 	else:
	# 		if time.time()-self.timestamp > 0.01:
	# 			self.timestamp = None


	def bounce(self, index):
		#collision left
		if index == 0:
			self.direction.x = -self.direction.x
			self.position.x -= 0.5
		#collision right 
		if index == 1:
			self.direction.x = -self.direction.x
			#self.position.x += 1
		#collision top
		if index == 2:
			self.direction.y = -self.direction.y
			self.position.y -= 0.5
		#collision bottom	
		if index == 3:
			self.direction.y = -self.direction.y
			#self.position.y += 1



	def move(self, deltaTime):
		if self.isMoving:
			self.position += self.direction * self.speed / deltaTime
			self.hitbox.center = (self.position.x, self.position.y)

			if self.position.x < 0:
				self.bounce(0)
			elif self.position.x > 640:
				self.bounce(1)
			if self.position.y < 0:
				self.bounce(2)
			elif self.position.y > 480:
				self.bounce(3)

			# if self.position.x >= self.rect.right-(self.radius/2) or self.position.x <= self.rect.left+(self.radius/2):
			# 	self.bounce(True)
			# if self.position.y >= self.rect.bottom or self.position.y-(self.radius/2) <= self.rect.bottom+(self.radius/2):
			# 	self.bounce(False)


	def checkForCollisions(self, list, persons):
		list2 = list[:]
		list2.remove(self.hitbox)
		
		index = self.hitbox.collidelist(list2)
		if index > -1:

			if (self.hitbox.center[0] + self.hitbox.right) > (list2[index].center[0] - list2[index].left) :
				self.bounce(0)
			elif self.hitbox.center[0] - self.hitbox.left < list2[index].center[0] + list2[index].right:
				self.bounce(1)
			
			if self.hitbox.center[1] - self.hitbox.top < list2[index].center[1] + list2[index].bottom:
				self.bounce(2)
			elif self.hitbox.center[1] + self.hitbox.bottom > list2[index].center[1] - list2[index].top:
				self.bounce(3)

			# if self.hitbox.center[0] - self.hitbox.left < list2[index].center[0]+list2[index].right or self.hitbox.center[0] + self.hitbox.right > list2[index].center[0]-list2[index].left:
			# 	self.bounce(True)
			# if self.hitbox.center[1] - self.hitbox.top < list2[index].center[1]+list2[index].bottom or self.hitbox.center[1] + self.hitbox.bottom > list2[index].center[1]-list2[index].top:
			# 	self.bounce(False)

			if persons[index].isInfected and persons[index].isAlive:
				self.infection(persons[index].virus.contagiousRate, persons[index].virus.pathToJson)

	########Infection########

	#Méthode lancée chaque cycle par une autre personne lorsqu'elle rentre en contact avec la personne courante.
	#Infecte la personne courante selon la chance d'infection passée en paramètre et avec le virus également passé en paramètre. 
	def infection(self, contagiousRate, pathToJson):
		if self.isAlive and not self.isInfected and not self.isCured:
			if self.equipment["mask"] == True :
				contagiousRate / 2
			if determineFrom(contagiousRate) == True :
				self.virus = Virus(self.age,self.healthIssues,pathToJson)
				self.infectionTime = time.time()
				self.willDie = determineFrom(self.virus.deathRate)
				self.isInfected = True

	def personUpdate(self):
		if self.isInfected:
			if self.willDie == True:
				if time.time()-self.infectionTime >= self.virus.deathTimer:
					self.isAlive = False
			else:
				if time.time()-self.infectionTime >= self.virus.healTimer:
					self.isInfected = False
					self.isCured = True
		self.updateColor()

	def updateColor(self):
		if self.isAlive:
			if self.isInfected:
				self.color = [255,0,0]
			elif self.isCured:
				self.color = [0,255,0]
		else:
			self.color = [0,0,0]
			self.isMoving = False

def generate(Rect, n = 100):
	persons = []
	while n > 0:
		persons.append(Person(Rect))
		n -= 1
	hitboxes = []
	for person in persons:
		hitboxes.append(person.hitbox)
	return persons, hitboxes