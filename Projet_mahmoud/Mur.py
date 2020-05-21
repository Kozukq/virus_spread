import pygame
from pygame.locals import *
from random import random
import sys

def EXIT():
    quitter = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == QUIT or quitter[K_ESCAPE]:
            pygame.quit(); sys.exit()

WHITE = (255, 255, 255)
rect = []
rect2 = []
pygame.init()

pygame.display.set_caption("RECT ({}, {})".format(640, 440))
Surface = pygame.display.set_mode((640, 440))


class Rectangle:
    def __init__(self, x, y, height):
        self.color = (88, 214, 141)
        self.x = x
        self.y = y
        self.width = 10
        self.height = height
        self.h = 5

rect.append(Rectangle(140, 0, 220))
rect2.append(Rectangle(140, 440, -220))


def Draw_Rect():
    """
        Fonction qui crée les cercles
    """
    Surface.fill(WHITE)
    for circle in rect:
        pygame.draw.rect(Surface, (145, 34, 234), (circle.x , circle.y, circle.width, circle.height))
    for circle2 in rect2:
        pygame.draw.rect(Surface, (145, 34, 234), (circle2.x , circle2.y, circle2.width, circle2.height))
    
    pygame.display.flip()

def Move_Rect1():
    """
        Fonction qui permet de bouger les cercles
    """
    for element in rect:
        element.height -= element.h
        pygame.time.Clock().tick(5)
    
def Move_Rect2():
    for e in rect2:
        e.height += e.h
        pygame.time.Clock().tick(5)

#pygame.draw.rect(Surface, color(rgb), (positions(int,int), dimensions(int,int)) )
"""pygame.draw.rect(Surface, (145,34,234), (140, 0, 10, 220))
pygame.draw.rect(Surface, (200,150,100), (140, 440, 10, -220))
pygame.display.flip()"""

def main():
    while True:
        EXIT()
        Draw_Rect()
        Move_Rect1()
        Move_Rect2()
if __name__ == '__main__': main()