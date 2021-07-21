from . import db
"""
    Aqui fazemos a importação do db que declaramos como
    global lá no nosso __init__ de app 
"""


class AlbumModel(db.Model):  # db.Model para criarmos a tabela
    __tablename__ = "albums"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    release_year = db.Column(db.String(9), nullable=False)
    band_id = db.Column(db.Integer, db.ForeignKey(
        'bands.id', onupdate="CASCADE", ondelete="CASCADE"))
    music_list = db.relationship('MusicModel', backref='album')
