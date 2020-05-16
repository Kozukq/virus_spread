import json

#Classe permettant de stocker les diverses informations a propos du virus
class Virus:
	def __init__(self, age : int, healthIssues : bool, pathToJson):
		self.pathToJson = pathToJson
		#open the json file	
		with open(pathToJson) as file:
			data = json.load(file)
			self.name = data["Name"]
			self.infectionChance = data["contagiousness"]
			#Chances de mourrir chaque cycle par age
			if age < 19:
				self.deathChance = data["DeathChance"]["10-19"]
			elif age < 29:
				self.deathChance = data["DeathChance"]["20-29"]
			elif age < 39:
				self.deathChance = data["DeathChance"]["30-39"]
			elif age < 49:
				self.deathChance = data["DeathChance"]["40-49"]
			elif age < 59:
				self.deathChance = data["DeathChance"]["50-59"]
			elif age < 69:
				self.deathChance = data["DeathChance"]["60-69"]
			elif age < 79:
				self.deathChance = data["DeathChance"]["70-79"]
			elif age < 89:
				self.deathChance = data["DeathChance"]["80-89"]
			else:
				self.deathChance = data["DeathChance"]["90-100"]

			#Multiplicateur de comorbidité
			if healthIssues:
				self.deathChance /= data["ComorbidityMultiplier"]


	def debug(self):
		print("Virus : ", self.name)
		print("Infection chance : ", self.infectionChance)
		print("Death chance : ", self.deathChance)


