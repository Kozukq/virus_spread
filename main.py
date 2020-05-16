import pygame
import sys
import time
import os
from src.person import Person, generate

#Pour gabriel qui utilise la magie noire afin de lancer les fenêtres sous windows#
# try:
#     os.environ["DISPLAY"]
# except:
#     os.environ["SDL_VIDEODRIVER"] = "dummy" 
##################################################################################

color = {
	"WHITE" : [255,255,255],
	"BLACK" : [0,0,0],
	"RED" : [255,0,0]
}

interface = ["menu","simulation"]

class Display:
	def __init__(self,width=640,height=480):
		self.width = width
		self.height = height
		self.window = pygame.display.set_mode([self.width,self.height])
		self.clock = pygame.time.Clock()

simulationWindow = Display()
menuWindow = Display()
currentWindow = interface[0]
population = 20
PersonList,HitboxList = generate(simulationWindow.window,population)
PersonList[0].infection(1, "Virus Presets/Covid.json")

def menuRendering():
	framerate = menuWindow.clock.tick(60)
	simulationWindow.window.fill(color["BLACK"])

def personRendering():
	framerate = simulationWindow.clock.tick(60)
	simulationWindow.window.fill(color["WHITE"])
	for person in PersonList:
		person.personUpdate()
		person.move(framerate)
		person.checkForCollisions(HitboxList,PersonList)
		person.draw()

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			#sys.exit()
			if currentWindow == interface[0] : currentWindow = interface[1]
			elif currentWindow == interface[1] : currentWindow = interface[0]
	if currentWindow == "menu" : menuRendering()
	elif currentWindow == "simulation" : personRendering()
	pygame.display.flip()