import pygame
import sys
import time
import os
from src.menu import Menu, Block, Button, TextBlock
from src.simulation import Simulation, color

class Window:
	def __init__(self,width=640,height=480):
		self.width = width
		self.height = height
		self.display = pygame.display.set_mode([self.width,self.height])
		self.clock = pygame.time.Clock()
		self.scene = "MENU"

pygame.init()
window = Window()
menu = Menu(window)
simulation = Simulation(window)

blockList = {
	"Button":Button(75, 40, pygame.Rect(10, window.display.get_height()-50, window.display.get_width()-20,40), "inside", "center", isVisible = False)
}
blockList["Text"] = TextBlock(75, 40, blockList["Button"].rect, "inside", "left", isVisible = False, text = "Stop", fontSize=30, padding = 7)



while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: 
			sys.exit()
	framerate = window.clock.tick(60)
	window.display.fill(color["WHITE"])
	if window.scene == "MENU" :
		menu.update()
		blockList["Button"].isVisible = False
		blockList["Text"].isVisible = False
		if menu.blockList["StartButton"].hasClicked():
			window.scene = "SIMULATION"
	elif window.scene == "SIMULATION" :
		if simulation.isStarted == True :
			simulation.run(framerate)
			for block in blockList:
				if blockList[block].isVisible:
					blockList[block].display(window.display)
			

			if len(simulation.stats.infected) <= 0:
				blockList["Button"].isVisible = True
				blockList["Text"].isVisible = True
				if blockList["Button"].hasClicked():
					simulation.stop()
					simulation.isStarted = False
					window.scene = "MENU"


		else :
			simulation.initialize(menu.population,menu.selectedJSON, menu.protected)
			simulation.isStarted = True
	pygame.display.flip()