from . import db
"""
    Aqui fazemos a importação do db a partir do app/models/__init__.py
"""


class BandModel(db.Model):  # db.Model para criação da tabela
    __tablename__ = "bands"
    """
        Aqui declaramos o nome da nossa tabela, caso __tablename__
        não seja declarado, o nome da tabela será o nome da classe
    """

    id = db.Column(db.Integer, primary_key=True)
    """
        * db.Column: para criação de coluna
        * db.Integer: indicando que essa coluna é um integer
        * primary_key = True: indicando que essa coluna é uma primary_key
    """

    name = db.Column(db.String(100), nullable=False, unique=True)
    """
        * db.Column: para criação de coluna
        * db.String(100): indicando que essa coluna é um varchar(100)
        * nullable = False: indicando que não será permitido valores nullos, 
          ele por default é definido como True.
        * unique = True: indicando que o nome da banda deve ser unico no nosso banco
    """
    albums = db.relationship('AlbumModel', backref='band')

    music_list = db.relationship('MusicModel', backref='band')
    """
        * db.relationship: para criação de relacionamentos
        * 'MusicModel': indicando a model (nome da classe) que irá se relacionar
        * backref='band': indicando qual tipo de relação está sendo feita
    """
