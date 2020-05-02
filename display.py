import pygame, sys, time, os
from Sim.person import Person
try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy" 

color = {
	"WHITE" : [255,255,255],
	"BLACK" : [0,0,0],
	"RED" : [255,0,0]
}

class display:
	def __init__(self):
		self.width = 320
		self.height = 240
		self.window = pygame.display.set_mode([self.width,self.height])

display = display()


while 1 :
	display.window.fill(color["BLACK"])
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	

	time.sleep(0.01)
	pygame.display.flip()
	