from flask import Flask
from flask import request
from werkzeug.contrib.atom import AtomFeed
from models import Noticia

app = Flask(__name__)

@app.route('/')
def Feed():
    feed = AtomFeed('Últimas Noticías do Diário do Nordeste',
                    feed_url=request.url, url=request.url_root)
    noticias = Noticia.select().order_by(Noticia.Data.desc())
    for noticia in noticias:
        feed.add(noticia.Titulo, noticia.Corpo,
                 id=noticia.id,
                 content_type='html',
                 author=noticia.Autor,
                 url=noticia.Link,
                 updated=noticia.Data)
    return feed.get_response()


if __name__ == '__main__':
    app.run()