from . import db
"""
    Aqui fazemos a importação do db que declaramos como
    global lá no nosso __init__ de app 
"""


class BandGenreModel(db.Model):  # db.Model para criarmos a tabela
    __tablename__ = "band_genres"
    """
        Aqui declaramos o nome da nossa tabela, caso __tablename__
        não seja declarado, o nome da tabela será o nome da classe
    """

    id = db.Column(db.Integer, primary_key=True)
    """
        * db.Column: para criação de coluna
        * db.Integer: indicando que essa coluna é um integer
        * primary_key=True: indicando que essa coluna é uma primary_key
    """

    band_id = db.Column(db.Integer, db.ForeignKey(
        'bands.id', onupdate='CASCADE', ondelete='CASCADE'))
    """
        * db.Column: para criação de coluna
        * db.Integer: indicando que essa coluna é um integer
        * db.ForeignKey: indicando a ForeingKey que vai ser recebida
        * bands.id: nome da tabela e o qual coluna deseja referenciar
        * onupdate='CASCADE': em caso de atualização de um registro desta tabela,
           todos os registros das tabelas que referenciam (ou são referenciados) por este 
           registro também serão atualizados
        * ondelete='CASCADE': em caso de deleção de um registro desta tabela,
           todos os registros das tabelas que referenciam (ou são referenciados) por este
           registro também serão deletados
    """

    genre_id = db.Column(db.Integer, db.ForeignKey(
        'genres.id', onupdate='CASCADE', ondelete='CASCADE'))
    """
        * db.Column: para criação de coluna
        * db.Integer: indicando que essa coluna é um integer
        * db.ForeignKey: indicando a ForeingKey que vai ser recebida
        * genres.id: nome da tabela e qual coluna deseja referenciar
        * onupdate='CASCADE': em caso de atualização de um registro desta tabela,
           todas os registros das tabelas que referenciam (ou são referenciados) por este
           registro também serão atualizados
        * ondelete='CASCADE': em caso de deleção de um registro desta tabela,
           todos os registros das tabelas que referenciam (ou são referenciados) por este
           registro também serão deletados
    """
