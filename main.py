import peewee
from crawler import *
from models import Noticia

def Main():
    crw = CrawlerNE()
    paginas = crw.listar_paginas()
    noticias = crw.listar_noticias(paginas)
    for link in noticias:
        noticia = crw.obter_notia(link)
        try:
            Noticia.insert(noticia).execute()
            print("Noticía {} adicionada com sucesso.".format(noticia['Titulo']))
        except peewee.IntegrityError:
            print("Noticía com o link {} já existe.".format(noticia['Link']))


if __name__ == '__main__':
    if not Noticia.table_exists():
        Noticia.create_table()
        print('Tabela Noticia Criada com Sucesso!')
    else:
        print('Tabela Noticia ja existe!')
    Main()