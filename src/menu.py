import pygame

class Menu:
	def __init__(self):
		# Attributes :

		# Affichage
		self.rect = pygame.Rect(0,0, 300, 200)

	def draw(self, Window):
		pygame.draw.rect(Window, [0,0,0], self.rect)