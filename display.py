import pygame
import sys
import time
import os
from src.person import Person, generate

#Pour gabriel qui utilise la magie noire afin de lancer les fenêtres sous windows#
try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy" 
##################################################################################

color = {
	"WHITE" : [255,255,255],
	"BLACK" : [0,0,0],
	"RED" : [255,0,0]
}

class Display:
	def __init__(self):
		self.width = 640
		self.height = 480
		self.window = pygame.display.set_mode([self.width,self.height])
		self.clock = pygame.time.Clock()

display = Display()

#Génère n personnes 
persons,hitboxes = generate(display.window,200)
persons[0].attributes["Infected"] = True
persons[0].color = [255,0,0]

#Fonction qui actualise l'affichage
def Render():
	display.window.fill(color["WHITE"])
	for person in persons :
		person.draw()
	pygame.display.flip()

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	deltaTime = display.clock.tick(60)

	for person in persons:
		person.move(deltaTime)
		person.checkForCollisions(hitboxes, persons)

	Render()