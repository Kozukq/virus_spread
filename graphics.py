import pygame, sys, time, os
try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy" 

WHITE = [255,255,255]
BLACK = [0,0,0]
RED = [255,0,0]
width = 320
height = 240
window = pygame.display.set_mode([width,height])

circle1 = pygame.draw.circle(window,WHITE,[width//4,height//2],10)
circle2 = pygame.draw.circle(window,WHITE,[(width//2+width//4),height//2],10)

pos1x = circle1.x
pos1y = circle1.y

pos2x = circle2.x
pos2y = circle2.y

color = WHITE

while 1 :
	window.fill(BLACK)
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	pos1x += 1
	pos2x -= 1

	circle1 = pygame.draw.circle(window,RED,[pos1x,pos1y],10)
	circle2 = pygame.draw.circle(window,color,[pos2x,pos2y],10)

	if circle1.right == circle2.left :
			color = RED

	time.sleep(0.01)
	pygame.display.flip()
	