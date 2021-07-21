from . import db
"""
    Aqui fazemos a importação do db a partir do app/models/__init__.py
"""


class MusicModel(db.Model):  # db.Model para criarmos a tabela
    __tablename__ = 'musics'
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

    name = db.Column(db.String(100), nullable=False)
    """
        * db.Column: para criação de coluna
        * db.String(100): indicando que essa coluna é um varchar(100)
        * nullable = False: indicando que não será permitido valores nullos, 
          ele por default é definido como True.
    """

    band_id = db.Column(db.Integer, db.ForeignKey('bands.id'))
    """
        * db.Column: para criação de coluna
        * db.Integer: indicando que essa coluna é um integer
        * db.ForeignKey: indicando a ForeingKey que vai ser recebida
        * bands.id: nome da tabela e qual coluna deseja referenciar, jutamente com qual coluna ela se relaciona
        * onupdate='CASCADE': em caso de atualização de um registro desta tabela,
           todas os registros das tabelas que referenciam (ou são referenciados) por este
           registro também serão atualizados
        * ondelete='CASCADE': em caso de deleção de um registro desta tabela,
           todos os registros das tabelas que referenciam (ou são referenciados) por este
           registro também serão deletados
    """
    album_id = db.Column(db.Integer, db.ForeignKey(
        'albums.id'))
