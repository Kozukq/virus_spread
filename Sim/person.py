import random
from Sim.utilities import decision
from Sim.utilities import namesList
from Sim.behavior import *
from Sim.virus import Virus


#Probabilité que la personne aie des problèmes de santé
probHealthIsues = 0.25

class Person:
	def __init__(self):
		self.name = random.choice(namesList)
		self.age = random.randint(10, 99)
		self.infected = False
		self.alive = True
		self.cured = False
		self.immunity = False
		self.healthIssues = decision(probHealthIsues)
		self.behavior = prudent

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

	def infection(self, pathToJson):
		if not self.immunity and self.alive:
			self.virus = Virus(self.age, self.healthIssues, pathToJson)
			self.infected = true
		


