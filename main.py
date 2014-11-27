__author__ = 'tales.cpadua'

import requests
import datetime
from bs4 import BeautifulSoup
import psycopg2

def is_movie(soup):
    for sherolero in soup.findAll('div', {'class': 'infobar'}):
            if(sherolero.contents[0].translate({ord(i): None for i in '_-'}).strip()) == "TV Episode":
                return False
            if(sherolero.contents[0].translate({ord(i): None for i in '_-'}).strip()) == "TV Series":
                return False
            if(sherolero.contents[0].translate({ord(i): None for i in '_-'}).strip()) == "TV Movie":
                return False
            else:
                return True
    return True

def get_soup(url):
    try:
        source_code = requests.get(url)
    except:
        return None
    if source_code.status_code == 404:
        print("404")
        return None
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)


    return soup

def crawler(paginas):
    # max_page = 133093
    # running = True
    visited_actors_links = []
    visited_directors_link = []
    null_pages = 0
    try:
        conn = psycopg2.connect("dbname='pifour' user='postgres' host='localhost' port=5432 password='suamae'")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()
    while True:
        if null_pages > 50:
            break
        print("reading page id number " + str(paginas))
        actors = []
        directors = []
        genres = []
        keywords = []
        countries = []
        null_pages = 0

        #Connections to profile pages take long time. Checking to avoid unnecessary connections. Hope it works =p
        launch_year = None

        soup = get_soup("http://www.imdb.com/title/tt" + str(paginas))
        if soup is None:
            null_pages += 1
            paginas += 1
            continue

        if not is_movie(soup):
            paginas += 1
            continue

        for dir_link in soup.findAll('h1', {'class': 'header'}):
            movie_name = dir_link.contents[1].string.strip()

        for link in soup.findAll('a', href=True):
            if "/year/" in link['href']:
                launch_year = link.string

        for infobar in soup.findAll('span', {'itemprop': 'genre'}):
            genres.append(infobar.string)

        for infobar in soup.findAll('a', {'itemprop': 'url'}, href=True):
            if "country" in infobar['href']:
                countries.append(infobar.string)

        for link in soup.findAll('div', {'itemprop': 'director'}):
            for dir_link in link.findAll('span', {'itemprop': 'name'}):
                country = False
                director_name = dir_link.string
                director_profile = dir_link.parent['href']
                if director_profile not in visited_directors_link:
                    visited_directors_link.append(director_profile)
                    director_soup = get_soup("http://www.imdb.com/" + director_profile)
                    if director_soup is not None:
                        for director_link in director_soup.findAll('a', href=True):
                            if "birth_place" in director_link['href']:
                                place = director_link.string.split(',')
                                birth_place = place[len(place)-1].strip()
                                country = True
                if country:
                    directors.append((director_name, birth_place))
                else:
                    directors.append((director_name, None))


        for link in soup.findAll('table', {'class', 'cast_list'}):
            cast_count = 0
            for tags in link.findAll('span', {'itemprop': 'name'}):
                country = False
                actor_name = tags.string
                actor_profile = tags.parent['href']
                if actor_profile not in visited_actors_links:
                    visited_actors_links.append(actor_profile)
                    actor_soup = get_soup("http://www.imdb.com/" + actor_profile)
                    if actor_soup is not None:
                        for actor_link in actor_soup.findAll('a', href=True):
                            if "birth_place" in actor_link['href']:
                                place = actor_link.string.split(',')
                                birth_place = place[len(place)-1].strip()
                                country = True
                if country:
                    actors.append((actor_name, birth_place))
                else:
                    actors.append((actor_name, None))
                #To avoid get data from too many secondary actors, I limited the number to 8
                cast_count += 1
                if cast_count > 7:
                    break

        for link in soup.findAll('span', {'itemprop': 'keywords'}):
            keyword = link.string
            keywords.append(keyword)

        #End crawling, start to put values to DATABASE

        print(movie_name + ", " + launch_year + " ")
        print(datetime.datetime.now().strftime("%y-%m-%d-%H-%M"))

        cur.execute("SELECT id FROM movies WHERE id = %s", (paginas,))
        if cur.fetchone() is None:
            cur.execute('INSERT INTO "movies" (id, name, release_date) '
                        'VALUES (%s, %s, %s)', (paginas, movie_name, launch_year))

        for genre in genres:
            cur.execute("SELECT genre FROM genres WHERE genre = %s", (genre,))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO genres (genre) VALUES (%s)", (genre,))
            cur.execute("SELECT * FROM genres WHERE genre = %s", (genre,))
            genre_object = cur.fetchone()
            cur.execute("INSERT INTO movie_genres (id_movie, id_genre) VALUES (%s, %s)", (paginas, genre_object[0]))

        for country in countries:
            cur.execute("SELECT country FROM countries WHERE country = %s", (country,))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO countries (country) VALUES (%s)", (country,))
            cur.execute("SELECT * FROM countries WHERE country = %s", (country,))
            country_object = cur.fetchone()
            cur.execute("INSERT INTO movie_countries (id_movie, id_country) VALUES (%s, %s)", (paginas, country_object[0]))

        for d in directors:
            cur.execute("SELECT name FROM directors WHERE name = %s", (d[0],))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO directors (name, country) VALUES (%s, %s)", (d[0], d[1]))
            cur.execute("SELECT * FROM directors WHERE name = %s", (d[0],))
            director_object = cur.fetchone()
            cur.execute("INSERT INTO movie_directors (id_movie, id_director)"
                        " VALUES (%s, %s)", (paginas, director_object[0]))

        for a in actors:
            cur.execute("SELECT name FROM actors WHERE name = %s", (a[0],))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO actors (name, country) VALUES (%s, %s)", (a[0], a[1]))
            cur.execute("SELECT * FROM actors WHERE name = %s", (a[0],))
            actor_object = cur.fetchone()
            cur.execute("INSERT INTO movie_actors (id_movie, id_actor)"
                        " VALUES (%s, %s)", (paginas, actor_object[0]))

        for k in keywords:
            cur.execute("SELECT keyword FROM keywords WHERE keyword = %s", (k,))
            if cur.fetchone() is None:
                cur.execute("INSERT INTO keywords (keyword) VALUES (%s)", (k,))
            cur.execute("SELECT * FROM keywords WHERE keyword = %s", (k,))
            keyword_object = cur.fetchone()
            cur.execute("INSERT INTO movies_keywords (id_movie, id_keyword) VALUES (%s, %s)", (paginas, keyword_object[0]))

        conn.commit()
        null_pages = 0
        paginas += 1

crawler(21781)