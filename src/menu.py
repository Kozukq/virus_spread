import pygame
import json
import os

class Menu:
	def __init__(self,Window):
		self.window = Window
		 
		self.selectedJSON = "Virus Presets/coronavirus.json"
		self.sliderCheck = False
		self.population = 100
		self.__maxPop = 200

		self.baseBottomRect = pygame.Rect(10, Window.display.get_height()-50, Window.display.get_width()-20,40)
		self.baseTopRect = pygame.Rect(10,10, Window.display.get_width(),50)

		self.blockList = {
			"BottomBlock":Block(75, 40, self.baseBottomRect, "inside", "right", False, 10),
			"TopBlock":Block(Window.display.get_width()-20,50, self.baseTopRect, "inside", "left", True)
		}
		self.blockList["Stats"] = Block(Window.display.get_width(), 350, self.blockList["TopBlock"].rect, "bottom", padding=10)
		self.blockList["name"] = TextBlock(Window.display.get_width(), 10, self.blockList["TopBlock"].rect, "bottom", padding=10, text="Name : ", fontSize = 15)
		self.blockList["contagiousRate"] = TextBlock(Window.display.get_width(), 10, self.blockList["name"].rect, "bottom", padding=10, text="Contagious rate : ", fontSize = 15)
		self.blockList["deathRate"] = TextBlock(Window.display.get_width(), 10, self.blockList["contagiousRate"].rect, "bottom", padding=10, text="Death rate : ", fontSize = 15)
		self.blockList["10-19"] = TextBlock(Window.display.get_width(), 10, self.blockList["deathRate"].rect, "bottom", padding=10, text="        10-19 : ", fontSize = 15)
		self.blockList["20-29"] = TextBlock(Window.display.get_width(), 10, self.blockList["10-19"].rect, "bottom", padding=10, text="        20-29 : ", fontSize = 15)
		self.blockList["30-39"] = TextBlock(Window.display.get_width(), 10, self.blockList["20-29"].rect, "bottom", padding=10, text="        30-39 : ", fontSize = 15)
		self.blockList["40-49"] = TextBlock(Window.display.get_width(), 10, self.blockList["30-39"].rect, "bottom", padding=10, text="        40-49 : ", fontSize = 15)
		self.blockList["50-59"] = TextBlock(Window.display.get_width(), 10, self.blockList["40-49"].rect, "bottom", padding=10, text="        50-59 : ", fontSize = 15)
		self.blockList["60-69"] = TextBlock(Window.display.get_width(), 10, self.blockList["50-59"].rect, "bottom", padding=10, text="        60-69 : ", fontSize = 15)
		self.blockList["70-79"] = TextBlock(Window.display.get_width(), 10, self.blockList["60-69"].rect, "bottom", padding=10, text="        70-79 : ", fontSize = 15)
		self.blockList["80+"] = TextBlock(Window.display.get_width(), 10, self.blockList["70-79"].rect, "bottom", padding=10, text="        80+ : ", fontSize = 15)
		self.blockList["ImpactOnWeaks"] = TextBlock(Window.display.get_width(), 10, self.blockList["80+"].rect, "bottom", padding=10, text="Impact on weaks : ", fontSize = 15)
		self.blockList["HealTimer"] = TextBlock(Window.display.get_width(), 10, self.blockList["ImpactOnWeaks"].rect, "bottom", padding=10, text="Heal Timer : ", fontSize = 15)
		self.blockList["DeathTimer"] = TextBlock(Window.display.get_width(), 10, self.blockList["HealTimer"].rect, "bottom", padding=10, text="Death Timer : ", fontSize = 15)
		self.blockList["Population"] = TextBlock(150, 20, self.blockList["DeathTimer"].rect, "bottom", padding = 10, text = "Population : ", fontSize = 15)
		self.blockList["sliderBar"] = Block(300, 10, self.blockList["Population"].rect, "right", padding = 20)
		self.blockList["sliderButton"] = Button(20,20, self.blockList["sliderBar"].rect, "inside", "center")
		self.blockList["sliderIcon"] = SpriteBlock(20,20, self.blockList["sliderButton"].rect, "inside", "center", imageSrc="resources/doublearrow.png")
		self.blockList["sliderText"] = TextBlock(40, 20, self.blockList["sliderBar"].rect, "right", padding = 20, text=str(self.population), fontSize=15)

		self.blockList["Protected"] = TextBlock(150, 20, self.blockList["Population"].rect, "bottom", padding = 10, text = "Amount of protected people : ", fontSize = 15)
		self.blockList["protectedBar"] = Block(300, 10, self.blockList["Protected"].rect, "right", padding = 20)
		self.blockList["protectedButton"] = Button(20,20, self.blockList["protectedBar"].rect, "inside", "center")
		self.blockList["protectedIcon"] = SpriteBlock(20,20, self.blockList["protectedButton"].rect, "inside", "center", imageSrc="resources/doublearrow.png")
		self.blockList["protectedText"] = TextBlock(40, 20, self.blockList["protectedBar"].rect, "right", padding = 20, text=str(self.population), fontSize=15)

		self.blockList["StartButton"] = Button(75, 40, self.blockList["BottomBlock"].rect, "inside", "left")
		self.blockList["StartText"] = TextBlock(75, 40, self.blockList["BottomBlock"].rect, "inside", "left", padding = 2, text = "Start")

		self.blockList["jsonText"] = TextBlock(500, 30, self.blockList["TopBlock"].rect, "inside", "left", padding=30, text="", fontSize = 20)
		self.blockList["jsonButton"] = Button(20, 20, self.blockList["TopBlock"].rect, "inside", "right", padding = 15)
		self.blockList["jsonArrow"] = SpriteBlock(20,20,self.blockList["TopBlock"].rect, "inside", "right", padding = 15, imageSrc = "resources/arrow.png")
		self.blockList["presets"] = []
		self.blockList["presets"].append(Block(0,0, self.blockList["jsonButton"].rect, "bottom"))

		self.blockList["jsonText"].textString = self.selectedJSON
		index = 0
		for file in os.listdir("Virus Presets"):
			self.blockList["presets"].append(Button(300, 50, self.blockList["presets"][index].rect, "bottom", padding=0, isVisible = False))
			self.blockList["presets"][index+1].rect.right = self.blockList["jsonButton"].rect.right
			self.blockList["presets"].append(TextBlock(100, 50, self.blockList["presets"][index+1].rect, "inside", "left", text=str(file), padding = 10, isVisible = False))
			index += 2


		self.load()
		

	def update(self):
		if self.blockList["jsonButton"].clickEvent():
			if not self.blockList["presets"][1].isVisible:
				self.blockList["jsonArrow"].imageSrc = "resources/arrow2.png"
			else:
				self.blockList["jsonArrow"].imageSrc = "resources/arrow.png"
			for block in self.blockList["presets"]:
				block.isVisible = not block.isVisible

		for index, preset in enumerate(self.blockList["presets"]):
			if isinstance(preset, Button):
				if preset.clickEvent():
					self.selectedJSON = "Virus Presets/"+self.blockList["presets"][index+1].textString
					self.blockList["jsonArrow"].imageSrc = "resources/arrow.png"
					self.load()
					for block in self.blockList["presets"]:
						block.isVisible = not block.isVisible

		if pygame.mouse.get_pos()[0] > self.blockList["sliderBar"].rect.left and pygame.mouse.get_pos()[0] < self.blockList["sliderBar"].rect.right:
			if self.blockList["sliderButton"].isHolding():
				self.blockList["sliderButton"].rect.center = pygame.mouse.get_pos()[0], self.blockList["sliderButton"].rect.center[1]
				self.population = int((self.blockList["sliderButton"].rect.center[0] - self.blockList["sliderBar"].rect.left) * self.__maxPop / self.blockList["sliderBar"].rect.width)+1
				self.blockList["sliderText"].textString = str(self.population)
				self.blockList["sliderIcon"].rect.center = self.blockList["sliderButton"].rect.center

		if pygame.mouse.get_pos()[0] > self.blockList["protectedBar"].rect.left and pygame.mouse.get_pos()[0] < self.blockList["protectedBar"].rect.right:
			if self.blockList["protectedButton"].isHolding():
				self.blockList["protectedButton"].rect.center = pygame.mouse.get_pos()[0], self.blockList["protectedButton"].rect.center[1]
				self.population = int((self.blockList["protectedButton"].rect.center[0] - self.blockList["protectedBar"].rect.left) * self.__maxPop / self.blockList["protectedBar"].rect.width)+1
				self.blockList["protectedText"].textString = str(self.population)
				self.blockList["protectedIcon"].rect.center = self.blockList["protectedButton"].rect.center

		self.render()
		

	def load(self):
		self.blockList["jsonText"].textString = "Path : \"" + self.selectedJSON + "\""
		with open(self.selectedJSON) as file:
			data = json.load(file)
			self.blockList["name"].textString = "Name : " + data["name"]
			self.blockList["contagiousRate"].textString = "Contagious rate : " + str(data["contagiousRate"])
			self.blockList["deathRate"].textString = "Death rate : "
			self.blockList["10-19"].textString = "        10-19 : " + str(data["deathRate"]["10-19"])
			self.blockList["20-29"].textString = "        20-29 : " + str(data["deathRate"]["20-29"])
			self.blockList["30-39"].textString = "        30-39 : " + str(data["deathRate"]["30-39"])
			self.blockList["40-49"].textString = "        40-49 : " + str(data["deathRate"]["40-49"])
			self.blockList["50-59"].textString = "        50-59 : " + str(data["deathRate"]["50-59"])
			self.blockList["60-69"].textString = "        60-69 : " + str(data["deathRate"]["60-69"])
			self.blockList["70-79"].textString = "        70-79 : " + str(data["deathRate"]["70-79"])
			self.blockList["80+"].textString = "        80+ : " + str(data["deathRate"]["80+"])
			self.blockList["ImpactOnWeaks"].textString = "Impact on weaks : " + str(data["impactOnWeaks"])
			self.blockList["HealTimer"].textString = "Heal Timer : " + str(data["healTimer"])
			self.blockList["DeathTimer"].textString = "Death Timer : " + str(data["deathTimer"])

			


	def render(self):
		for block in self.blockList:
			if not isinstance(self.blockList[block], list):
				if self.blockList[block].isVisible:
					self.blockList[block].display(self.window.display)
			else:
				for block in self.blockList["presets"]:
					if block.isVisible:
						block.display(self.window.display)




class Block:
	def __init__(self, width, height, parentRect = pygame.Rect(0,0,0,0), anchor = "bottom", centering="center", padding = 0, isVisible = True):
		self.rect = pygame.Rect(0,0, width, height)
		self.color = [255,255,204]
		self.border = True
		self.isVisible = isVisible
		self.test = False
		#Positionnement 
		if anchor == "bottom":
			self.rect.top = parentRect.bottom + padding
			self.rect.width -= padding*2
			self.rect.center = self.rect.center[0]+padding, self.rect.center[1]
		elif anchor == "top":
			self.rect.bottom = parentRect.top - padding
			self.rect.width -= padding*2
			self.rect.center = self.rect.center[0]+padding, self.rect.center[1]
		elif anchor == "left":
			self.rect.right = parentRect.left - padding
			self.rect.center = self.rect.center[0], parentRect.center[1]
		elif anchor == "right":
			self.rect.left = parentRect.right + padding
			self.rect.center = self.rect.center[0], parentRect.center[1]
		elif anchor == "inside":
			if centering == "left":
				self.rect.left = parentRect.left + padding
				self.rect.center = self.rect.center[0], parentRect.center[1]
			elif centering == "center":
				self.rect.center = parentRect.center
			elif centering == "right":
				self.rect.right = parentRect.right - padding
				self.rect.center = self.rect.center[0], parentRect.center[1]


	def display(self, Surface):
		pygame.draw.rect(Surface, self.color, self.rect)
		if self.border == True:
			pygame.draw.rect(Surface, [0,0,0], self.rect, 1)

class Button(Block):


	def hasClicked(self):
		if self.isVisible:
			return pygame.mouse.get_pressed()[0] and pygame.mouse.get_pos()[0] > self.rect.left and pygame.mouse.get_pos()[0] < self.rect.right and pygame.mouse.get_pos()[1] < self.rect.bottom and pygame.mouse.get_pos()[1] > self.rect.top

	def clickEvent(self):
		if self.isVisible:
			if self.test:
				if self.hasClicked():
					self.test = False
					return True

	def isHovering(self):
		if self.isVisible and not pygame.mouse.get_pressed()[0]:
			self.test = True
			return pygame.mouse.get_pos()[0] > self.rect.left and pygame.mouse.get_pos()[0] < self.rect.right and pygame.mouse.get_pos()[1] < self.rect.bottom and pygame.mouse.get_pos()[1] > self.rect.top

	def isHolding(self):
		self.clickEvent()
		if self.test == False:
			return True

		
			

	def display(self, Surface):
		pygame.draw.rect(Surface, self.color, self.rect)
		if self.isHovering():
			self.color = [255, 230, 153]
		else:
			self.color = [255, 255, 204]
		if self.isHolding():
			self.color = [255, 179, 153]
		if self.border == True:
			pygame.draw.rect(Surface, [0,0,0], self.rect, 1)


class TextBlock(Block):
	def __init__(self, width, height, parentRect = pygame.Rect(0,0,0,0), anchor = "bottom", centering="center", padding = 0, isVisible = True, text = "", fontSize = 30):
		super().__init__(width, height, parentRect, anchor, centering, padding, isVisible)
		self.textColor = [0,0,0]
		self.fontSize = fontSize
		self.font = pygame.font.Font("resources/fonts.ttf",self.fontSize)
		self.antialiasing = True
		self.textString = text
		self.border = False

		if anchor == "bottom":
			self.rect.left += padding


	def display(self, Surface):
		# pygame.draw.rect(Surface, self.color, self.rect)

		self.s = pygame.Surface((self.rect.width, self.rect.height))
		self.s.set_alpha(0)
		self.s.fill((255, 255, 255))
		self.__text = self.font.render(self.textString, self.antialiasing, self.textColor)
		Surface.blit(self.s, self.rect)
		Surface.blit(self.__text,self.rect)
		if self.border == True:
			pygame.draw.rect(Surface, [0,0,0], self.rect, 1)

class SpriteBlock(Block):
	def __init__(self, width, height, parentRect = pygame.Rect(0,0,0,0), anchor = "bottom", centering="center", padding = 0,  isVisible = True, imageSrc = ""):
		super().__init__(width, height, parentRect, anchor, centering, padding, isVisible)
		self.imageSrc = imageSrc
		self.border = False
		

	def display(self, Surface):
		self.s = pygame.Surface((self.rect.width, self.rect.height))
		self.s.set_alpha(0)
		self.s.fill((255, 255, 255))
		Surface.blit(self.s, self.rect)
		self.image = pygame.image.load(self.imageSrc)
		Surface.blit(self.image, self.rect.topleft)
		if self.border == True:
			pygame.draw.rect(Surface, [0,0,0], self.rect, 1)
