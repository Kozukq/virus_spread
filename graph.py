import pygame

pygame.init()
display = pygame.display.set_mode([640,480])







while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
	display.fill([255,255,255])
	pygame.draw.line(display,[0,0,0],[10,10],[10,470])
	pygame.display.flip()

class Stats():
	def __init__(self,personList):
		self.healthy = []
		self.infected = []

	def update(self):
		