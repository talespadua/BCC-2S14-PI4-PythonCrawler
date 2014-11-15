__author__ = 'tales.cpadua'

import requests

from bs4 import BeautifulSoup
import psycopg2

def get_soup(url):
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text)
    return soup

def crawler(paginas):
    max_page = 133093
    # try:
    #     conn = psycopg2.connect("dbname='imdbinfo' user='postgres' host='localhost' password='senha'")
    # except:
    #     print("I am unable to connect to the database")

    while paginas <= max_page:

        atores = []
        diretores = []
        escritores = []
        produtores = []
        generos = []

        #Here the crawler get info on main Movie page
        # url = "http://www.imdb.com/title/tt" + str(pagina)
        # source_code = requests.get(url)
        # plain_text = source_code.text
        soup = get_soup("http://www.imdb.com/title/tt" + str(paginas))

        for infobar in soup.findAll('span', {'itemprop': 'genre'}):
            generos.append(infobar.string)
            print(infobar.string)

        # for infobar in soup.findAll('a', {'title': 'See all release dates'}):
        #     pais_de_origem = infobar.contents[2].strip().translate({ord(i): None for i in '()'})
        #     print(pais_de_origem + "\n")

        #Here the crawler get info on movie fullcredits page
        # url = "http://www.imdb.com/title/tt" + str(pagina) + "/fullcredits"
        # source_code = requests.get(url)
        # plain_text = source_code.text
        soup = get_soup("http://www.imdb.com/title/tt" + str(paginas) + "/fullcredits")

        for dir_link in soup.findAll('div', {'class': 'parent'}):
            nome_filme = dir_link.h3.a.string.strip()
            ano = dir_link.h3.span.string.strip().translate({ord(i): None for i in '()'})
            print(nome_filme + "\n" + ano + "\n")

        for dir_link in soup.findAll('h4', {'class': 'dataHeaderWithBorder'}):
            cabecalho = dir_link.contents[0].strip()
            if cabecalho == "Directed by":
                print(cabecalho)
                body_tag = dir_link.findNext('tbody')
                for tags in body_tag.findAll('a'):
                    link = tags['href']
                    diretores.append(tags.string.strip())
                    print(tags.string.strip())
                    dir_soup = get_soup("http://www.imdb.com/" + link)
                    for link in dir_soup.findAll('a', href=True):
                        if "birth_place" in link['href']:
                            place = link.string.split(',')
                            birth_place = place[len(place)-1].strip()
                            print(birth_place)


            # if cabecalho == "Writing Credits":
            #     print(cabecalho)
            #     body_tag = dir_link.findNext('tbody')
            #     for tags in body_tag.findAll('a'):
            #         escritores.append(tags.string.strip())
            #         print(tags.string.strip())
            #

            if cabecalho == "Cast":
                print(cabecalho)
                body_tag = dir_link.findNext('table')
                for tags in body_tag.findAll('td', {'class': 'itemprop'}):
                    atores.append(tags.a.span.string.strip())
                    print(tags.a.span.string.strip())

            #
            # if cabecalho == "Produced by":
            #     print(cabecalho)
            #     body_tag = dir_link.findNext('tbody')
            #     for tags in body_tag.findAll('a'):
            #         produtores.append(tags.string.strip())
            #         print(tags.string.strip())

        paginas += 1

crawler(133092)