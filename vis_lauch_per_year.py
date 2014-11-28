import requests

import psycopg2

import os, sys
import pygame
from pygame.locals import *

try:
    conn = psycopg2.connect("dbname='pifour' user='postgres' host='localhost' port=5432 password='senha'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

cur.execute('SELECT COUNT(%s) as num_movies, release_date FROM movies GROUP BY release_date'
			' ORDER BY release_date', ("movies", ))

movie_years = cur.fetchall()

for movie in movie_years:
	print movie

screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

screen.fill((255, 255, 255))
printed = False
pos_y = 0
pos_x = 0

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	if printed is False:
		for movie in movie_years:
			y_size = movie[0]*0.3
			if y_size < 1:
				y_size = 1
			pygame.draw.rect(screen, (200, 100, 0), Rect((pos_x, pos_y), (screen_width/movie_years.__len__(), y_size)))
			pos_x = pos_x + screen_width/movie_years.__len__()
			
		printed = True
	screen.lock()

	screen.unlock()

	pygame.display.update()