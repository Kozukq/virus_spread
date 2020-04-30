import pygame, sys

WHITE = [255,255,255]
width = 320
height = 240
center = [width//2,height//2]
window = pygame.display.set_mode([width,height])

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	circle = pygame.draw.circle(window,WHITE,center,10)



	pygame.display.flip()
	