import pygame

width = 320
height = 240
window = pygame.display.set_mode([width,height])

basicColor = pygame.Color(0,0,0)

circle = pygame.draw.circle(window,basicColor,[150,150],1)

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()
	