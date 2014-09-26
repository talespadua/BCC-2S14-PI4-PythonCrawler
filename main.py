__author__ = 'tales.cpadua'

import requests
from bs4 import BeautifulSoup

def crawler(paginas):
    pagina = 133093
    while pagina <= paginas:
        url = "http://www.imdb.com/title/tt" + str(pagina)
        source_code = requests.get(url)
        plain_text = source_code.text
        soup = BeautifulSoup(plain_text)
        for link in soup.findAll('td', {'id': 'overview-top'}):
            title = link.h1.span.string
            time = link.time.get("datetime")
            print("Title: " + title)
            print("Time: " + time)

            # Header do Filme
            '''for header in link.findAll('div', {'class': 'infobar'}):
                # Selecione todas os spans que possuem como atributo o valor genre
                genre = header.select('span[itemprop=genre]')

                # Lista todos os generos do filme
                for item in genre:
                    print("Genero: " + item.string)'''

        pagina += 1



crawler(133093)