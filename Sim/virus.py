import json

#Classe permettant de stocker les diverses informations a propos du virus
class Virus:
	def __init__(self, age : int, healthIssues : bool, pathToJson):
		#open the json file	
		with open(pathToJson) as jsonFile:
			self.settings = json.load(jsonFile)
			self.name = settings["Name"]
			self.infectionChance = settings["infectionChance"]
			#Chances de mourrir chaque cycle par age
			if age < 19:
				self.deathChance = settings["DeathChance"]["10-19"]
			elif age < 29:
				self.deathChance = settings["DeathChance"]["20-29"]
			elif age < 39:
				self.deathChance = settings["DeathChance"]["30-39"]
			elif age < 49:
				self.deathChance = settings["DeathChance"]["40-49"]
			elif age < 59:
				self.deathChance = settings["DeathChance"]["50-59"]
			elif age < 69:
				self.deathChance = settings["DeathChance"]["60-69"]
			elif age < 79:
				self.deathChance = settings["DeathChance"]["70-79"]
			elif age < 89:
				self.deathChance = settings["DeathChance"]["80-89"]
			else:
				self.deathChance = settings["DeathChance"]["90-100"]
			if healthIssues:
				self.deathChance *= settings["ComorbidityMultipplier"]


	def printVirus(self):
		print("Virus : ", self.name)
		print("Infection chance : ", self.infectionChance)
		print("Death chance : ", self.deathChance)


