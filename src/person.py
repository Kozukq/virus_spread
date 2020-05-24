import pygame

import random
import time
import random
from src.behavior import behaviorTypes
from src.virus import Virus

def determineFrom(probability):
	return random.random() < probability

namesList = ["Ben", "Gabriel", "Jupiler", "Passepartout", "Bill", "François", "Toumou", "Jacques-Etienne", "Le Montagnard", "Le Pingouin", "Oualoulou", "Chewbacca", "Bubul"]		

#Classe permettant de représenter une personne
class Person:
	def __init__(self, Rect, protectionChance, psychoChance):
		#Données brutes sur la personne
		self.name = random.choice(namesList)
		self.age = random.randint(10,99)
		self.isAlive = True
		self.isInfected = False
		self.isCured = False
		self.healthIssues = determineFrom(0.25)

		#Comportement de la personne
		self.behavior = random.choices(list(behaviorTypes.items), k=protectionChance)
		if self.behavior.name == "Uncareful":
			self.behavior.isPsycho = determineFrom(psychoChance)
			self.target = None

		#################################### Graphics part ###################################################
		#Position de la personne dans l'espace
		self.rect = Rect
		self.position = pygame.math.Vector2(random.randint(self.rect.left+20, self.rect.right-20), random.randint(self.rect.top+20,self.rect.bottom-20))
		self.radius = 7
		self.color = [200,200,200]
		self.width = 0
		#Vecteur normalisé représentant la direction
		self.direction = pygame.math.Vector2(random.uniform(-1,1), random.uniform(-1, 1)).normalize()
		self.hitbox = pygame.Rect((self.position.x)-5, (self.position.y)-5, self.radius*1.5, self.radius*1.5)
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
		#pygame.draw.rect(Window, [0,0,0], self.hitbox,1)

	def moveTowards(self, target, deltaTime):
		self.position += (target - self.position).normalize() * self.behavior.speed / deltaTime

	def bounce(self, index):
		#collision left
		if index == 0:
			self.direction.x = abs(self.direction.x)
			
		#collision right 
		if index == 1:
			self.direction.x = -(abs(self.direction.x))
			
		#collision top
		if index == 2:
			self.direction.y = abs(self.direction.y)
			
		#collision bottom	
		if index == 3:
			self.direction.y = -(abs(self.direction.y))
			
	def move(self, deltaTime):
		if self.isMoving:
			if not self.behavior.isPsycho or (self.behavior.isPsycho and not self.isInfected):
				self.position += self.direction * self.behavior.speed / deltaTime
				self.hitbox.center = (self.position.x, self.position.y)

				if self.position.x < self.rect.left + self.radius:
					self.bounce(0)
				elif self.position.x > self.rect.right - self.radius:
					self.bounce(1)
				if self.position.y < self.rect.top + self.radius:
					self.bounce(2)
				elif self.position.y > self.rect.bottom - self.radius:
					self.bounce(3)
			else: 
				if self.target:
					if self.target.isInfected:
						self.target = None
					else:
						self.moveTowards(self.target, deltaTime)
				

	def getTarget(self, healthyPeople):
		self.target = random.choice(healthyPeople)




	def checkForCollisions(self, OriginalHitboxList, PersonList):
		HitboxList = OriginalHitboxList[:]
		HitboxList.remove(self.hitbox)
		firstCollision = self.hitbox.collidelist(HitboxList)
		if firstCollision > -1:
			if self.hitbox.center[0] > HitboxList[firstCollision].center[0] and self.hitbox.left < HitboxList[firstCollision].right:
				self.bounce(0)
			if self.hitbox.center[0] < HitboxList[firstCollision].center[0] and self.hitbox.right > HitboxList[firstCollision].left:
				self.bounce(1)
			if self.hitbox.center[1] > HitboxList[firstCollision].center[1] and self.hitbox.top < HitboxList[firstCollision].bottom:
				self.bounce(2)
			if self.hitbox.center[1] < HitboxList[firstCollision].center[1] and self.hitbox.bottom > HitboxList[firstCollision].top:
				self.bounce(3)

			if self.isAlive and self.isInfected:
				for person in PersonList:
					if person.hitbox == HitboxList[firstCollision]:
						person.infection(self.virus)

	########Infection########

	def firstInfection(self,JSON):
		self.virus = Virus(self.age,self.healthIssues,JSON)
		self.infectionTime = time.time()
		self.willDie = determineFrom(self.virus.deathRate)
		self.isInfected = True


	#Méthode lancée chaque cycle par une autre personne lorsqu'elle rentre en contact avec la personne courante.
	#Infecte la personne courante selon la chance d'infection passée en paramètre et avec le virus également passé en paramètre. 
	def infection(self,virus):
		contagiousRate = virus.contagiousRate
		if self.isAlive and not self.isInfected and not self.isCured:
			if self.equipment["mask"] == True :
				contagiousRate = 0
			if determineFrom(contagiousRate) == True :
				self.virus = Virus(self.age,self.healthIssues,virus.JSON)
				self.infectionTime = time.time()
				self.willDie = determineFrom(self.virus.deathRate)
				self.isInfected = True

	def update(self):
		#Gestion du temps de pause :
		if self.isInfected == True:
			if self.willDie == True:
				if time.time() - self.infectionTime >= self.virus.deathTimer:
					self.isAlive = False
			else:
				if time.time() - self.infectionTime >= self.virus.healTimer:
					self.isInfected = False
					self.isCured = True
		self.updateColor()

	def updateColor(self):
		if self.isAlive:
			if self.equipment["mask"] == True :
				self.color = [150,150,150]
			if self.isInfected:
				self.color = [255,0,0]
			elif self.isCured:
				self.color = [0,255,0]
		else:
			self.color = [0,0,0]
			self.isMoving = False
