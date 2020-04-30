import random
from Sim.parameters import decision


#Probabilité que la personne aie des problèmes de santé
probHealthIsues = 0.25

class Person:
	def __init__(self):
		self.age = random.randint(10, 99)
		self.infected = False
		self.alive = True
		self.cured = False
		self.immunity = False
		self.healthIssues = decision(probHealthIsues)

	def displayInfos(self):
		print("Infos : ")
		print("Age : ", self.age)
		print("Infected : ", self.infected)
		print("Cured : ", self.cured)
		print("Is immune : ", self.immunity)
		print("Has existing health issues : ", self.healthIssues)


