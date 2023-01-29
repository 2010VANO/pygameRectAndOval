import pygame
import sys


pygame.init()

win = pygame.display.set_mode((600, 600))
win.fill((225, 225, 225))
rect = pygame.Rect(50, 250, 200, 100)
pygame.draw.rect(win, (225, 225, 0), rect, 0)
oval = (250, 50, 100, 200)
pygame.draw.circle(win, (0, 225, 0), oval, 0)
pygame.display.update()


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()



