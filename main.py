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
        diretores = []
        escritores = []
        for dir_link in soup.findAll('div', {'class': 'parent'}):
            nome_filme = dir_link.h3.a.string.strip()
            ano = dir_link.h3.span.string.strip()
            print(nome_filme + ano)

        for dir_link in soup.findAll('h4', {'class': 'dataHeaderWithBorder'}):
            cabecalho = dir_link.contents[0].strip()
            if cabecalho == "Directed by":
                print(cabecalho)
                body_tag = dir_link.findNext('tbody')
                for tags in body_tag.findAll('a'):
                    print(tags.string.strip())

            if cabecalho == "Writing Credits":
                print(cabecalho)
                body_tag = dir_link.findNext('tbody')
                for tags in body_tag.findAll('a'):
                    print(tags.string.strip())

            if cabecalho == "Cast":
                print(cabecalho)
                body_tag = dir_link.findNext('table')
                for tags in body_tag.findAll('td', {'class': 'itemprop'}):
                    print(tags.a.span.string.strip())

            if cabecalho == "Produced by":
                print(cabecalho)
                body_tag = dir_link.findNext('tbody')
                for tags in body_tag.findAll('a'):
                    print(tags.string.strip())


        '''for actorlink in soup.findAll('td', {'itemprop': 'actor'}):
            #title = link.h1.span.string
            #time = link.time.get("datetime")
            #print("Title: " + title)
            #print("Time: " + time)
            #atores.__add__(self, nome)
            nome = actorlink.a.span.string
            atores.append(nome)
            #print(nome)'''

        pagina += 1

crawler(133093)