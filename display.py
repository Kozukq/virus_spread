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


display = Display()
clock = pygame.time.Clock()

#Génère n personnes 
persons = generate(display.window,200)
rectList = []
for person in persons:
	rectList.append(person.hitbox)

#Fonction qui actualise l'affichage
def Render():
	display.window.fill(color["WHITE"])
	for person in persons :
		person.draw()


	pygame.display.flip()

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	deltaTime = clock.tick(60)

	for person in persons:
		person.move(50/float(deltaTime))

	Render()