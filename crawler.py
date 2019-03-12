import requests
from bs4 import *


base_url = 'https://diariodonordeste.verdesmares.com.br'


class CrawlerNE:
    def listar_paginas(self):
        links = []
        source = requests.get(base_url + '/servicos/ultima-hora').text
        soup = BeautifulSoup(source, 'html.parser')
        table = soup.find('div', {'class': 'c-pagination__center'})
        itens = table.findAll('a')
        for item in itens:
            links.append(item['href'])
        return links

    def listar_noticias(self,links):
        noticias = []
        for link in links:
            source = requests.get(base_url+link).text
            soup = BeautifulSoup(source, 'html.parser')
            table = soup.find('div',{'class': 'l-column'})
            itens = table.findAll('article')
            for item in itens:
                link = item.a['href']
                noticias.append(link)
        return noticias

    def obter_notia(self,link):
        source = requests.get(base_url + link).text
        soup = BeautifulSoup(source, 'html.parser')
        struct = soup.find('div', {'itemtype': 'http://schema.org/Article'})
        titulo = struct.find('h1', {'class': 'c-article__heading'}).text
        editorial = struct.find('a', {'class': 'c-tools__link'}).text
        autor = struct.find('span', {'itemprop': 'author'}).text
        data = struct.find('time')['datetime']
        lide = struct.find('h2', {'class': 'c-article__subheading'}).text
        content = struct.find('div', {'class': 'c-article-content'})
        corpo = ''
        for item in content.findAll('p'):
            corpo += item.text + '\n'
        noticia = {
            'Titulo': titulo,
            'Autor': autor,
            'Data': data,
            'Editorial': editorial,
            'Lide': lide,
            'Corpo': corpo,
            'Link': base_url + link
        }
        return noticia