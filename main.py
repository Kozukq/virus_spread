import pygame
import sys
import time
import os
from src.person import Person, generate

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

#Classe permettant de stocker les différentes statistiques
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

	def draw(self,rect,window):
		text_healthy = self.font.render("Healthy : " + str(len(self.healthy)),self.antialiasing,color["BLACK"])
		text_infected = self.font.render("Infected : " + str(len(self.infected)),self.antialiasing,color["BLACK"])
		text_dead = self.font.render("Dead : " + str(len(self.dead)),self.antialiasing,color["BLACK"])
		text_cured = self.font.render("Cured : " + str(len(self.cured)),self.antialiasing,color["BLACK"])
		window.blit(text_healthy,rect)
		rect = rect.move(0,self.fontSize)
		window.blit(text_infected,rect)
		rect = rect.move(0,self.fontSize)
		window.blit(text_dead,rect)
		rect = rect.move(0,self.fontSize)
		window.blit(text_cured,rect)


	def debug(self):
		print("Healthy : ", len(self.healthy))
		print("Infected : ", len(self.infected))
		print("Dead : ", len(self.dead))
		print("Cured : ", len(self.cured))
#Start
pygame.init()

window = Window()

statRect = pygame.Rect(10,0,window.width,100)
simuRect = pygame.Rect(0,statRect.bottom,window.width,window.height-statRect.height)

population = 200
PersonList,HitboxList = generate(simuRect,population)
PersonList[0].infection(1, "Virus Presets/coronavirus.json")
stats = Stats(PersonList)

def personRendering():
	pygame.draw.rect(window.display,color["BLACK"],simuRect,1)
	for person in PersonList:
		person.update()
		person.move(framerate)
		person.checkForCollisions(HitboxList,PersonList)
		person.draw(window.display)

def statRendering():
	stats.update()
	stats.draw(statRect,window.display)

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
	framerate = window.clock.tick(60)
	window.display.fill(color["WHITE"])
	personRendering()
	statRendering()
	pygame.display.flip()