import json

#Classe permettant de stocker les diverses informations a propos du virus
class Virus:
	def __init__(self, age : int, healthIssues : bool, JSON):
		self.JSON = JSON
		self.name = None
		self.contagiousRate = 0
		self.deathRate = 0
		self.deathTimer = 0
		self.healTimer = 0
		#open the json file	
		with open(JSON) as file:
			data = json.load(file)
			self.name = data["name"]
			self.contagiousRate = data["contagiousRate"]
			#Chances de mourir chaque cycle par age
			if age < 19:
				self.deathRate = data["deathRate"]["10-19"]
			elif age < 29:
				self.deathRate = data["deathRate"]["20-29"]
			elif age < 39:
				self.deathRate = data["deathRate"]["30-39"]
			elif age < 49:
				self.deathRate = data["deathRate"]["40-49"]
			elif age < 59:
				self.deathRate = data["deathRate"]["50-59"]
			elif age < 69:
				self.deathRate = data["deathRate"]["60-69"]
			elif age < 79:
				self.deathRate = data["deathRate"]["70-79"]
			else:
				self.deathRate = data["deathRate"]["80+"]

			self.healTimer = data["healTimer"]
			self.deathTimer = data["deathTimer"]
			#Multiplicateur de comorbidité
			if healthIssues:
				self.deathRate *= data["impactOnWeaks"]
				self.deathTimer /= data["impactOnWeaks"]
				self.healTimer *= data["impactOnWeaks"]


	def debug(self):
		print("Virus : ", self.name)
		print("Death chance : ", self.deathRate)


