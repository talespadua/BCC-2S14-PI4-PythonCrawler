import requests

import psycopg2

import os, sys
import pygame
from pygame.locals import *

try:
    conn = psycopg2.connect("dbname='pifour' user='postgres' host='localhost' port=5435 password='senha'")
except:
    print("I am unable to connect to the database")

cur = conn.cursor()

cur.execute('SELECT release_date, genre, MAX(quant) maxquant '
			'FROM ' 
			
			'(SELECT movies.release_date, genres.genre, COUNT(genre) AS quant FROM movie_genres '
			'INNER JOIN genres ON movie_genres.id_genre = genres.id '
			'INNER JOIN movies ON movies.id = movie_genres.id '
			'GROUP BY release_date, genre ORDER BY release_date, quant DESC) tabela1 '
			
			'GROUP BY release_date, genre ORDER BY release_date, genre ')
			#(SELECT release_date FROM movies))

genres = cur.fetchall()

lista = []

print(range(len(genres)))

max_genre = None

for i in range(len(genres)):
	if genres[i][0] != genres[(i - 1)][0]:
		if max_genre is None:
			max_genre = genres[i]
		else:
			lista.append(max_genre)
			max_genre = genres[i]
		continue
	else:
		if genres[i][2] > max_genre[2]:
			max_genre = genres[i]

for l in lista:
	print l

screen_width = 640*2
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height), 0, 32)

pygame.init()

myfont = pygame.font.SysFont("arial", 8)
sub_font = pygame.font.SysFont("arial", 15)

screen.fill((255, 255, 255))
printed = False
pos_y = 0
pos_x = 0

drama_color = (100,230,76)
short_color = (125,125,125)
animation_color = (0,255,255)
comedy_color = (255,0,67)
crime_color = (255,67,0)
western_color = (78,44,9)
sub_pos = 25
subtitles = []

while True:
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()

	if printed is False:
		for genre in lista:
			y_size = genre[2]
			
			pos_y = 471 - y_size
			if genre[1] == "Drama":
				cor = drama_color
			if genre[1] == "Short":
				cor = short_color
			if genre[1] == "Animation":
				cor = animation_color
			if genre[1] == "Western":
				cor = western_color
			if genre[1] == "Crime":
				cor = crime_color
			if genre[1] == "Comedy":
				cor = comedy_color

			pygame.draw.rect(screen, cor, Rect((pos_x, pos_y), (screen_width/lista.__len__() - 2, y_size)))

			pygame.draw.rect(screen, drama_color, Rect((100, 20), (25, 25)))
			subtitles.append(sub_font.render("Drama", 1, (0,0,0)))

			pygame.draw.rect(screen, short_color, Rect((100, 50), (25, 25)))
			subtitles.append(sub_font.render("Short", 1, (0,0,0)))

			pygame.draw.rect(screen, animation_color, Rect((100, 80), (25, 25)))
			subtitles.append(sub_font.render("Animation", 1, (0,0,0)))

			pygame.draw.rect(screen, comedy_color, Rect((100, 110), (25, 25)))
			subtitles.append(sub_font.render("Comedy", 1, (0,0,0)))

			pygame.draw.rect(screen, crime_color, Rect((100, 140), (25, 25)))
			subtitles.append(sub_font.render("Crime", 1, (0,0,0)))

			pygame.draw.rect(screen, western_color, Rect((100, 170), (25, 25)))
			subtitles.append(sub_font.render("Western", 1, (0,0,0)))


			pos_x = pos_x + screen_width/lista.__len__() + 1
			label = myfont.render(str(genre[0]), 1, (0,0,0))
			pygame.transform.rotate(label, 90)
			screen.blit(label, (pos_x, 470))

			screen.blit(subtitles[0], (10, 25))
			screen.blit(subtitles[1], (10, 55))
			screen.blit(subtitles[2], (10, 85))
			screen.blit(subtitles[3], (10, 115))
			screen.blit(subtitles[4], (10, 145))
			screen.blit(subtitles[5], (10, 175))	

		printed = True
	screen.lock()

	screen.unlock()

	pygame.display.update()