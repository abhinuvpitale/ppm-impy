import pygame
import sys
import numpy as np
import ppmimpy as ppy

pygame.init()
print('4:1 Screen Size \nClick to flip colours')
screen = pygame.display.set_mode((128*4,32*4))
arr = np.zeros((32,128))
black = (0,0,0)
white= (255,255,255)
ppmfile = ppy.ppmimpy()
while 1:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			print('Bye! Saving Image to temp.ppm')
			ppmfile.array_to_image(arr)
			ppmfile.create_file('temp')	
			pygame.quit()
			sys.exit()
		if event.type == pygame.MOUSEBUTTONDOWN:
			x,y = pygame.mouse.get_pos()
			x = int(x/4)
			y = int(y/4)
			old = arr[y][x]
			arr[y][x] = 1 if old == 0 else 0
			pygame.draw.rect(screen,white if arr[y][x]==1 else black,(4*x,4*y,4,4),0)
 
			print(x,y)
			pygame.display.update()
