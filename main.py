import pygame
import sys
import time
import os
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

class GraphLine:
	def __init__(self,healthyLength,infectedLength,deadLength,curedLength,xPosition,yPosition):
		self.healthy = pygame.Rect(xPosition,yPosition,1,healthyLength)
		self.infected = pygame.Rect(xPosition,self.healthy.bottom,1,infectedLength)
		self.dead = pygame.Rect(xPosition,self.infected.bottom,1,deadLength)
		self.cured = pygame.Rect(xPosition,self.dead.bottom,1,curedLength)

class Stats:
	def __init__(self,window,population,statRect,personList):
		self.healthy = personList[:]
		self.infected = []
		self.dead = []
		self.cured = []
		self.fontSize = 20
		self.font = pygame.font.Font("resources/fonts.ttf",self.fontSize)
		self.antialiasing = True
		self.statRect = statRect
		self.textRect = pygame.Rect(self.statRect.left,self.statRect.top,200,self.statRect.height)
		self.graphRect = pygame.Rect(self.textRect.right+50,self.statRect.top+10,self.statRect.width-self.textRect.width-100,self.statRect.height-20)
		self.population = population
		self.lastLinePosition = self.graphRect.left+1
		self.graphLines = []
		self.window = window

	def update(self):
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


	def drawText(self):
		text_healthy = self.font.render("Healthy : " + str(len(self.healthy)),self.antialiasing,color["BLACK"])
		text_infected = self.font.render("Infected : " + str(len(self.infected)),self.antialiasing,color["BLACK"])
		text_dead = self.font.render("Dead : " + str(len(self.dead)),self.antialiasing,color["BLACK"])
		text_cured = self.font.render("Cured : " + str(len(self.cured)),self.antialiasing,color["BLACK"])
		drawingRect = self.textRect 
		self.window.display.blit(text_healthy,drawingRect)
		drawingRect = drawingRect.move(0,self.fontSize)
		self.window.display.blit(text_infected,drawingRect)
		drawingRect = drawingRect.move(0,self.fontSize)
		self.window.display.blit(text_dead,drawingRect)
		drawingRect = drawingRect.move(0,self.fontSize)
		self.window.display.blit(text_cured,drawingRect)


	def graphUpdate(self):
		healthyLength = (len(self.healthy) / self.population) * self.graphRect.height
		infectedLength = (len(self.infected) / self.population) * self.graphRect.height
		deadLength = (len(self.dead) / self.population) * self.graphRect.height
		curedLength = (len(self.cured) / self.population) *self.graphRect.height
		self.graphLines.append(GraphLine(healthyLength,infectedLength,deadLength,curedLength,self.lastLinePosition,self.graphRect.top+1))

	def drawGraph(self):
		pygame.draw.rect(self.window.display,[0,0,0],self.graphRect,1)
		if self.lastLinePosition < self.graphRect.right :
			self.lastLinePosition += 1
		else :
			self.graphLines.remove(self.graphLines[0])
			for line in self.graphLines:
				line.healthy = line.healthy.move(-1,0)
				line.infected = line.infected.move(-1,0)
				line.dead = line.dead.move(-1,0)
				line.cured = line.cured.move(-1,0)
		for line in self.graphLines:
			pygame.draw.rect(self.window.display,[0,0,255],line.healthy)
			pygame.draw.rect(self.window.display,[255,0,0],line.infected)
			pygame.draw.rect(self.window.display,[0,0,0],line.dead)
			pygame.draw.rect(self.window.display,[0,255,0],line.cured)

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
		self.stats = Stats(self.window,self.population,self.statRect,self.personList)

	def personRendering(self,framerate):
		pygame.draw.rect(self.window.display,color["BLACK"],self.simuRect,1)
		for person in self.personList:
			person.update()
			person.move(framerate)
			person.checkForCollisions(self.hitboxList,self.personList)
			person.draw(self.window.display)

	def statRendering(self):
		self.stats.update()
		self.stats.graphUpdate()
		self.stats.drawText()
		self.stats.drawGraph()

	def run(self,framerate):
		self.personRendering(framerate)
		self.statRendering()

	def stop(self):
		print("coming soon")

pygame.init()
window = Window()
menu = Menu(window)
simulation = Simulation(window)

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
		if window.scene == "MENU" and event.type == pygame.KEYDOWN:
				if event.key == pygame.K_RETURN:
					window.scene = "SIMULATION"
	framerate = window.clock.tick(60)
	window.display.fill(color["WHITE"])
	if window.scene == "MENU" :
		menu.update()
		if menu.blockList["StartButton"].hasClicked():
			window.scene = "SIMULATION"
	elif window.scene == "SIMULATION" :
		if simulation.isStarted == True :
			simulation.run(framerate)
		else :
			simulation.initialize(200,menu.selectedJSON)
			simulation.isStarted = True
	pygame.display.flip()