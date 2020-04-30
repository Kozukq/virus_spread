import pygame, sys, time, os

try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy" 

WHITE = [255,255,255]
width = 320
height = 240
center = [width//2,height//2]
window = pygame.display.set_mode([width,height])
position = [0,0]
backward = False

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	print(position)
	if backward :
		circle = pygame.draw.circle(window,WHITE,position,10)
	else :
		circle = pygame.draw.circle(window,WHITE,position,10)


	if circle.left < 0 or circle.right > width :
		backward = True
		position[0] = 0
	if circle.top < 0 or circle.bottom > height :
		backward = True
		position[1] = 0
	else :
		position[0] += 1
		position[1] += 1

	pygame.display.flip()
	