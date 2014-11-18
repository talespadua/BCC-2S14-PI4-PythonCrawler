__author__ = 'tales.cpadua'

import requests

from bs4 import BeautifulSoup
#import psycopg2

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
    source_code = requests.get(url)
    if source_code.status_code == 404:
        print("404")
        return None
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    return soup

def crawler(paginas):
    max_page = 133093
    running = True
    # try:
    #     conn = psycopg2.connect("dbname='imdbinfo' user='postgres' host='localhost' password='senha'")
    # except:
    #     print("I am unable to connect to the database")

    #while running:
    while paginas <= max_page:

        atores = []
        diretores = []
        escritores = []
        produtores = []
        generos = []
        nullPages = 0
        #Here the crawler get info on main Movie page

        soup = get_soup("http://www.imdb.com/title/tt" + str(paginas))
        if soup is None:
            nullPages += 1
            paginas += 1
            continue

        if not is_movie(soup):
            paginas += 1
            continue

        for dir_link in soup.findAll('h1', {'class': 'header'}):
            movie_name = dir_link.contents[1].string.strip()
            print(movie_name)

        for link in soup.findAll('a', href=True):
            if "/year/" in link['href']:
                print(link.string)

        for infobar in soup.findAll('span', {'itemprop': 'genre'}):
            generos.append(infobar.string)
            print(infobar.string)

        for infobar in soup.findAll('a', {'itemprop': 'url'}, href=True):
            if "country" in infobar['href']:
                movie_country = infobar.string
                print(movie_country)

        for link in soup.findAll('table', {'class', 'cast_list'}):
            cast_count = 0
            for tags in link.findAll('span', {'itemprop': 'name'}):
                print(tags.string)
                cast_count += 1
                if cast_count > 7:
                    break

        #Here the crawler get info on movie fullcredits page

        # soup = get_soup("http://www.imdb.com/title/tt" + str(paginas) + "/fullcredits")
        #
        # for dir_link in soup.findAll('h4', {'class': 'dataHeaderWithBorder'}):
        #     cabecalho = dir_link.contents[0].strip()
        #     if cabecalho == "Directed by":
        #         print(cabecalho)
        #         body_tag = dir_link.findNext('tbody')
        #         for tags in body_tag.findAll('a'):
        #             link = tags['href']
        #             diretores.append(tags.string.strip())
        #             print(tags.string.strip())
        #             dir_soup = get_soup("http://www.imdb.com/" + link)
        #             for link in dir_soup.findAll('a', href=True):
        #                 if "birth_place" in link['href']:
        #                     place = link.string.split(',')
        #                     birth_place = place[len(place)-1].strip()
        #                     print(birth_place)


            # if cabecalho == "Writing Credits":
            #     print(cabecalho)
            #     body_tag = dir_link.findNext('tbody')
            #     for tags in body_tag.findAll('a'):
            #         escritores.append(tags.string.strip())
            #         print(tags.string.strip())


            # if cabecalho == "Cast":
            #     cast_count = 0
            #     print(cabecalho)
            #     body_tag = dir_link.findNext('table')
            #     for tags in body_tag.findAll('td', {'class': 'itemprop'}):
            #         link = tags.a['href']
            #         atores.append(tags.a.span.string.strip())
            #         print(tags.a.span.string.strip())
            #         dir_soup = get_soup("http://www.imdb.com/" + link)
            #         for link in dir_soup.findAll('a', href=True):
            #             if "birth_place" in link['href']:
            #                 place = link.string.split(',')
            #                 birth_place = place[len(place)-1].strip()
            #                 print(birth_place)
            #         cast_count += 1
            #         if cast_count > 7:
            #             break

            # if cabecalho == "Produced by":
            #     print(cabecalho)
            #     body_tag = dir_link.findNext('tbody')
            #     for tags in body_tag.findAll('a'):
            #         produtores.append(tags.string.strip())
            #         print(tags.string.strip())
        nullPages = 0
        paginas += 1

crawler(133093)