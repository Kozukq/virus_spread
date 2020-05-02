import pygame
import sys
import time
import os
from src.person import Person
try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy" 

color = {
	"WHITE" : [255,255,255],
	"BLACK" : [0,0,0],
	"RED" : [255,0,0]
}

class Display:
	def __init__(self):
		self.width = 320
		self.height = 240
		self.window = pygame.display.set_mode([self.width,self.height])

display = Display()


while 1 :
	display.window.fill(color["BLACK"])
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	

	time.sleep(0.01)
	pygame.display.flip()