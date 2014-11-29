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

cur.execute('SELECT release_date, genre, MAX(quant) maxquant '
			'FROM ' 
			
			'(SELECT movies.release_date, genres.genre, COUNT(genre) AS quant FROM movie_genres '
			'INNER JOIN genres ON movie_genres.id_genre = genres.id '
			'INNER JOIN movies ON movies.id = movie_genres.id '
			'GROUP BY release_date, genre ORDER BY release_date, quant DESC) tabela1 '
			
			'GROUP BY release_date, genre ORDER BY release_date, genre ')
			#(SELECT release_date FROM movies))

actor_countries = cur.fetchall()

print actor_countries