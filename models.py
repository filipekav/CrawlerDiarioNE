import peewee

db = peewee.SqliteDatabase('DiarioNE.db')


class Noticia(peewee.Model):
    Titulo = peewee.CharField()
    Autor = peewee.CharField()
    Data = peewee.DateTimeField()
    Editorial = peewee.CharField()
    Lide = peewee.TextField()
    Corpo = peewee.TextField()
    Link = peewee.CharField(unique=True)

    class Meta:
        database = db