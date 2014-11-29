import requests

import psycopg2

import os, sys
import pygame
from pygame.locals import *

try:
    conn = psycopg2.connect("dbname='pifour' user='postgres' host='localhost' port=5432 password='suamae'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

cur.execute('SELECT COUNT(%s) as num_country, country FROM actors GROUP BY country'
			' ORDER BY num_country DESC LIMIT 11', ("country", ))

actor_countries = cur.fetchall()

print actor_countries

transform_constant = 0.002

country_images = []

country_images.append(pygame.image.load("images/United_States.jpg"))
country_images.append(pygame.image.load("images/United_Kingdom.jpg"))
country_images.append(pygame.image.load("images/Germany.jpg"))
country_images.append(pygame.image.load("images/France.jpg"))
country_images.append(pygame.image.load("images/Sweden.jpg"))
country_images.append(pygame.image.load("images/Italy.jpg"))
country_images.append(pygame.image.load("images/Denmark.jpg"))
country_images.append(pygame.image.load("images/Spain.jpg"))
country_images.append(pygame.image.load("images/Canada.jpg"))
country_images.append(pygame.image.load("images/Poland.jpg"))

for i, images in enumerate(country_images):
	images = pygame.transform.scale(images, (int(68*actor_countries[(i+1)][0]*transform_constant), int(34*actor_countries[(i+1)][0]*transform_constant)))
	country_images[i] = images

for images in country_images:
	print images.get_width()

screen_width = 900
screen_height = 650
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

pos_x = 0
pos_y = 0
printed = False
screen.fill((255, 255, 255))

while True:
	
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	if printed is False:
		for image in country_images:
			screen.blit(image, (pos_x, pos_y))
			pos_x = pos_x + image.get_width()
			if pos_x > screen_width:
				pos_x = 0
				pos_y = pos_y + country_images[0].get_height()
		printed = True
	screen.lock()

	screen.unlock()

	pygame.display.update()