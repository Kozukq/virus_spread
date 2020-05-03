import pygame
import sys
import time
import os
from src.person import Person

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

persons = []
persons.append(Person(display.window))
persons[0].center()

#Fonction qui actualise l'affichage
def Render():
	display.window.fill(color["WHITE"])
	for person in persons :
		person.draw()


	pygame.display.flip()

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	

	Render()
	
	#trouver un autre moyen de limiter le framerate car pendant le sleep toute la simulation est bloquée
	time.sleep(1)