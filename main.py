import pygame
import sys
import time
import os
#from src.person import Person, generate
from src.person import Person
from src.menu import Menu
from src.virus import Virus

color = {
	"WHITE" : [255,255,255],
	"BLACK" : [0,0,0],
	"RED" : [255,0,0]
}

class Window:
	def __init__(self,width=640,height=480):
		self.width = width
		self.height = height
		self.display = pygame.display.set_mode([self.width,self.height])
		self.clock = pygame.time.Clock()
		self.scene = "MENU"

class Stats:
	def __init__(self,personList):
		self.healthy = personList[:]
		self.infected = []
		self.dead = []
		self.cured = []
		self.fontSize = 20
		self.font = pygame.font.Font("resources/fonts.ttf",self.fontSize)
		self.antialiasing = True 

	def update(self):
		#self.debug()
		for person in self.healthy:
			if person.isInfected:
				self.infected.append(person)
				self.healthy.remove(person)
		for person in self.infected:
			if not person.isAlive:
				self.dead.append(person)
				self.infected.remove(person)
			elif person.isCured:
				self.cured.append(person)
				self.infected.remove(person)

	def draw(self,rect,Surface):
		text_healthy = self.font.render("Healthy : " + str(len(self.healthy)),self.antialiasing,color["BLACK"])
		text_infected = self.font.render("Infected : " + str(len(self.infected)),self.antialiasing,color["BLACK"])
		text_dead = self.font.render("Dead : " + str(len(self.dead)),self.antialiasing,color["BLACK"])
		text_cured = self.font.render("Cured : " + str(len(self.cured)),self.antialiasing,color["BLACK"])
		Surface.blit(text_healthy,rect)
		rect = rect.move(0,self.fontSize)
		Surface.blit(text_infected,rect)
		rect = rect.move(0,self.fontSize)
		Surface.blit(text_dead,rect)
		rect = rect.move(0,self.fontSize)
		Surface.blit(text_cured,rect)


	def debug(self):
		print("Healthy : ", len(self.healthy))
		print("Infected : ", len(self.infected))
		print("Dead : ", len(self.dead))
		print("Cured : ", len(self.cured))

class Simulation:
	def __init__(self,Window):
		self.window = Window
		self.population = 0
		self.statRect = pygame.Rect(10,0,self.window.width,100)
		self.simuRect = pygame.Rect(0,self.statRect.bottom,self.window.width,self.window.height-self.statRect.height)
		self.personList = []
		self.hitboxList = []
		self.stats = None
		self.isStarted = False

	def generate(self):
		for i in range(0,self.population):
			self.personList.append(Person(self.simuRect))
		for person in self.personList:
			self.hitboxList.append(person.hitbox)

	def initialize(self,population,virus):
		self.population = population
		self.generate()
		self.personList[0].firstInfection(virus)
		self.stats = Stats(self.personList)

	def personRendering(self,framerate):
		pygame.draw.rect(self.window.display,color["BLACK"],self.simuRect,1)
		for person in self.personList:
			person.update()
			person.move(framerate)
			person.checkForCollisions(self.hitboxList,self.personList)
			person.draw(self.window.display)

	def statRendering(self):
		self.stats.update()
		self.stats.draw(self.statRect,self.window.display)

	def run(self,framerate):
		self.personRendering(framerate)
		self.statRendering()

	def stop(self):
		print("coming soon")

pygame.init()
window = Window()
menu = Menu(window)
simulation = Simulation(window)

# statRect = pygame.Rect(10,0,window.width,100)
# simuRect = pygame.Rect(0,statRect.bottom,window.width,window.height-statRect.height)
# population = 200
# PersonList,HitboxList = generate(simuRect,population)
# PersonList[0].infection(1, "Virus Presets/coronavirus.json")
# stats = Stats(PersonList)

# menu = Menu()
# toggleMenu = False

# def personRendering():
# 	pygame.draw.rect(window.display,color["BLACK"],simuRect,1)
# 	for person in PersonList:
# 		person.update()
# 		person.move(framerate)
# 		person.checkForCollisions(HitboxList,PersonList)
# 		person.draw(window.display)

# def statRendering():
# 	stats.update()
# 	stats.draw(statRect,window.display)

# def menuRendering():
# 	if toggleMenu == True:
# 		menu.draw(window.display)


# def togglePause():
# 	for person in PersonList:
# 		person.isMoving = not person.isMoving
# 		person.isPaused = not person.isPaused

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		# if window.scene == "MENU" and event.type == pygame.KEYDOWN:
		# 		if event.key == pygame.K_RETURN:
		# 			window.scene = "SIMULATION"
		# if event.type == pygame.KEYDOWN:
		# 	if event.key == pygame.K_a:
		# 		toggleMenu = not toggleMenu
		# 		togglePause()
	framerate = window.clock.tick(60)
	window.display.fill(color["WHITE"])

	if window.scene == "MENU" :
		menu.render(window)
		# if menu.hasClicked():
		# 	window.scene = "SIMULATION"
	elif window.scene == "SIMULATION" :
		if simulation.isStarted == True :
			simulation.run(framerate)
		else :
			simulation.initialize(200,"Virus Presets/coronavirus.json")
			simulation.isStarted = True
	# personRendering()
	# statRendering()
	# menuRendering()
	pygame.display.flip()