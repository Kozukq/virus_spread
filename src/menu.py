import pygame

class Menu:
	def __init__(self,Window):
		# Attributes :
		self.window = Window
		self.fontSize = 30
		self.font = pygame.font.Font("resources/fonts.ttf",self.fontSize)
		self.antialiasing = True 

		self.virus = {
			"name": "Coronavirus",
			"contagiousRate": 0.5,
			"deathRate": { 
				"10-19":0.002,
				"20-29":0.002,
				"30-39":0.002,
				"40-49":0.004,
				"50-59":0.013,
				"60-69":0.036,
				"70-79":0.08,
				"80+":0.148
			},
			"impactOnWeaks":1,
			"healTimer":5,
			"deathTimer":5
		}

		# Affichage

		self.blockList = []
		self.blockList.append(Block(Window.display.get_width(), 50))
		self.blockList.append(Block(Window.display.get_width(), 50, self.blockList[0].rect, "bottom"))
		self.blockList.append(Block(Window.display.get_width(), 50, self.blockList[1].rect, "bottom"))

		# self.rect = pygame.Rect(0,0,self.window.width,self.window.height)
		# self.rectText = pygame.Rect(90,210,100,50)
		# self.rectButton = pygame.Rect(90, self.rectText.bottom, 100, 50)
		# self.rectButton.center = self.window.width/2, self.rectButton.center[1]


	# def draw(self,Surface):
	# 	pygame.draw.rect(Surface,[0,0,0],self.rect)
	# 	welcomeText = self.font.render("Press START to start the simulation",self.antialiasing,[255,255,255])
	# 	pygame.draw.rect(Surface, [255,255,255], self.rectButton)
	# 	startText = self.font.render("START",self.antialiasing,[0,0,0])
	# 	Surface.blit(welcomeText,self.rectText)
	# 	Surface.blit(startText, self.rectButton)

	def render(self,Window):
		#self.draw(Window.display)
		for block in self.blockList:
			block.display(Window.display)

	# def hasClicked(self):
	# 	# if pygame.mouse.get_pressed()[0]:
	# 	# 	if pygame.mouse.get_pos()[0] > self.rectButton.left and pygame.mouse.get_pos()[0] < self.rectButton.right and pygame.mouse.get_pos()[1] < self.rectButton.bottom and pygame.mouse.get_pos()[1] > self.rectButton.top:
	# 	# 		return True

class Block:
	def __init__(self, width, height, parentRect = pygame.Rect(0,0,0,0), anchor = "bottom", centering="centered", padding = 10):
		self.rect = pygame.Rect(0,0, width, height)
		if anchor == "bottom":
			self.rect.top = parentRect.bottom + padding
		elif anchor == "top":
			self.rect.bottom = parentRect.top - padding
		elif anchor == "left":
			self.rect.right = parentRect.left - padding
		elif anchor == "right":
			self.rect.left = parentRect.right + padding
		# elif anchor == "inside":
		# 	self.rect.left 


	def display(self, Surface):
		pygame.draw.rect(Surface, [255,255,204], self.rect)
		pygame.draw.rect(Surface, [0,0,0], self.rect, 1)