__author__ = 'tales.cpadua'

import requests
from bs4 import BeautifulSoup

def crawler(paginas):
    pagina = 133093
    while pagina <= paginas:
        url = "http://www.imdb.com/title/tt" + str(pagina) + "/fullcredits"
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        atores = []

        for dir_link in soup.findAll('h4', {'class': 'dataHeaderWithBorder'}):
            cabecalho = dir_link.string
            if cabecalho == "Directed by ":
                print(cabecalho)
                body_tag = dir_link.findNext('tbody')
                for tags in body_tag.findAll('a'):
                    print(tags.string.strip())


        for actorlink in soup.findAll('td', {'itemprop': 'actor'}):
            #title = link.h1.span.string
            #time = link.time.get("datetime")
            #print("Title: " + title)
            #print("Time: " + time)
            #atores.__add__(self, nome)
            nome = actorlink.a.span.string
            atores.append(nome)
            #print(nome)

        pagina += 1

crawler(133093)