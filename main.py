import pygame
import sys
import time
import os
from src.person import Person, generate

pygame.init()

color = {
	"WHITE" : [255,255,255],
	"BLACK" : [0,0,0],
	"RED" : [255,0,0]
}

class Display:
	def __init__(self,width=640,height=480):
		self.width = width
		self.height = height
		self.window = pygame.display.set_mode([self.width,self.height])
		self.clock = pygame.time.Clock()

#Classe permettant de stocker les différentes statistiques
class Stats:
	def __init__(self,personList):
		self.healthy = personList[:]
		self.infected = []
		self.dead = []
		self.cured = []

	def statUpdate(self):
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

	def draw(self,rect,window):
		text_healthy = pygame.font.SysFont("impact",30).render("Healthy : " + str(len(self.healthy)),False,[0,0,0])
		text_infected = pygame.font.SysFont("impact",30).render("Infected : " + str(len(self.infected)),False,[0,0,0])
		text_dead = pygame.font.SysFont("impact",30).render("Dead : " + str(len(self.dead)),False,[0,0,0])
		text_cured = pygame.font.SysFont("impact",30).render("Cured : " + str(len(self.cured)),False,[0,0,0])
		window.blit(text_healthy,rect)
		rect = rect.move(0,30)
		window.blit(text_infected,rect)
		rect = rect.move(0,30)
		window.blit(text_dead,rect)
		rect = rect.move(0,30)
		window.blit(text_cured,rect)


	def debug(self):
		print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
		print("Healthy : ", len(self.healthy))
		print("Infected : ", len(self.infected))
		print("Dead : ", len(self.dead))
		print("Cured : ", len(self.cured))

window = Display()
simulation = pygame.Rect(0,0,500,480)
statistics = pygame.Rect(simulation.right,0,(window.width-simulation.width),480)
population = 200
PersonList,HitboxList = generate(simulation,population)
PersonList[0].infection(1, "Virus Presets/coronavirus.json")
stats = Stats(PersonList)

def personRendering():
	framerate = window.clock.tick(60)
	window.window.fill(color["WHITE"])
	pygame.draw.rect(window.window, [0,0,0], simulation, 1)
	for person in PersonList:
		person.personUpdate()
		person.move(framerate)
		person.checkForCollisions(HitboxList,PersonList)
		person.draw(window.window)

def statRendering():
	#window.window.fill(color["WHITE"])
	stats.statUpdate()
	stats.draw(statistics,window.window)

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
	personRendering()
	statRendering()
	pygame.display.flip()