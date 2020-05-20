import pygame

class Menu:
	def __init__(self,Window):
		# Attributes :
		self.window = Window
		self.fontSize = 30
		self.font = pygame.font.Font("resources/fonts.ttf",self.fontSize)
		self.antialiasing = True 

		# Affichage
		self.rect = pygame.Rect(0,0,self.window.width,self.window.height)
		self.rectText = pygame.Rect(90,210,100,50)

	def draw(self,Surface):
		pygame.draw.rect(Surface,[0,0,0],self.rect)
		welcomeText = self.font.render("Press ENTER to start the simulation",self.antialiasing,[255,255,255])
		Surface.blit(welcomeText,self.rectText)

	def render(self,Window):
		self.draw(Window.display)