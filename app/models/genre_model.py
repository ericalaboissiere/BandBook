from . import db
"""
    Aqui fazemos a importação do db a partir do app/models/__init__.py
"""


class GenreModel(db.Model):  # db.Model para criarmos a tabela
    __tablename__ = 'genres'
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
        * nullable=False: indicando que não será permitido valores null,
          ele por default é definido como True
        * unique=True: estamos indicando que essa coluna vai ter valor único
    """

    band_list = db.relationship(
        'BandModel', backref='genre_list', secondary='band_genres')
    """
        * db.relationship: para criação de relacionamentos
        * 'BandModel': indicando a model (nome da classe) que irá se relacionar
        * backref='genre_list': indicando qual tipo de relação está sendo feita
        * secondary='band_genres': nome da tabela pivo entre essa relação N:N
    """
