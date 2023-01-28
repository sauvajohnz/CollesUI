import sys
import pygame


size = width, height = 1000, 600
pygame.init()
screen = pygame.display.set_mode(size)
pygame.display.flip()
running = True
while running is True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
