__author__ = 'tales.cpadua'

import requests

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
    max_page = 133093
    running = True
    try:
        conn = psycopg2.connect("dbname='pifour' user='postgres' host='localhost' port=5435 password='senha'")
    except:
        print("I am unable to connect to the database")

    cur = conn.cursor()
    #while running:
    while paginas <= max_page:
        print("reading page id number " + str(paginas))
        actors = []
        directors = []
        genres = []
        keywords = []
        null_pages = 0
        launch_year = None

        #Here the crawler get info on main Movie page
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
                movie_country = infobar.string

        for link in soup.findAll('div', {'itemprop': 'director'}):
            for dir_link in link.findAll('span', {'itemprop': 'name'}):
                country = False
                director_name = dir_link.string
                director_profile = dir_link.parent['href']
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
                actor_profile = tags.parent['href']
                actor_name = tags.string
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
                cast_count += 1
                if cast_count > 7:
                    break

        for link in soup.findAll('span', {'itemprop': 'keywords'}):
            keyword = link.string
            keywords.append(keyword)

        print(movie_name + ", " + movie_country + ", " + launch_year)
        #insert movie values
        # cur.execute('INSERT INTO "movies" (id, name, release_date) '
        #             'VALUES (%s, %s, %s)', (paginas, movie_name, launch_year))

        for genre in genres:
            print(genre)

        for d in directors:
            print(d[0] + ", " + d[1])

        for a in actors:
            print(a[0] + ", " + a[1])

        for k in keywords:
            print(k)
        #insert genre values
        # cur.execute('INSERT INTO "genres" (name, country)c

        conn.commit()
        null_pages = 0
        paginas += 1

crawler(133093)