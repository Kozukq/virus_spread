import pygame, sys, time, os
try:
    os.environ["DISPLAY"]
except:
    os.environ["SDL_VIDEODRIVER"] = "dummy" 

WHITE = [255,255,255]
BLACK = [0,0,0]
width = 320
height = 240
window = pygame.display.set_mode([width,height])

circle1 = pygame.draw.circle(window,WHITE,[width/4,height/2],10)
circle2 = pygame.draw.circle(window,WHITE,[(width/2+width/4),height/2],10)

speed1 = [1,2]
speed2 = [-1,0]

while 1 :
	for event in pygame.event.get():
		if event.type == pygame.QUIT: sys.exit()

	circle1.move(speed1)
	circle2.move(speed2)

	circle1 = pygame.draw.circle(window,WHITE,[circle1.x,circle1.y],10)
	circle2 = pygame.draw.circle(window,WHITE,[circle2.x,circle2.y],10)

	# window.fill(BLACK)
	time.sleep(0.1)
	pygame.display.flip()
	