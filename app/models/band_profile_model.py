from . import db 
"""
    Aqui fazemos a importação do db a partir do app/models/__init__.py
"""
class BandProfileModel(db.Model): # db.Model para criarmos a tabela
    __tablename__ = 'band_profiles' 
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

    state = db.Column(db.String, nullable=False) 
    """
        * db.Column: para criação de coluna
        * db.String: indicando que essa coluna é um varchar(255)
        * nullable = False: indicando que não será permitido valores nullos, 
          ele por default é definido como True.
    """

    country = db.Column(db.String, nullable=False) 
    """
        * db.Column: para criação de coluna
        * db.String: indicando que essa coluna é um varchar(255)
        * nullable = False: indicando que não será permitido valores nullos, 
          ele por default é definido como True.
    """

    ein = db.Column(db.String(9), unique=True, nullable=False) 
    """
        * db.Column: para criação de coluna
        * db.String: indicando que essa coluna é um varchar(9)
        * nullable = False: indicando que não será permitido valores nullos, 
           ele por default é definido como True.
        * unique = True: indicando que o ein deve ser unico no nosso banco
    """

    band_id = db.Column(db.Integer, db.ForeignKey(
        'bands.id', onupdate="CASCADE", ondelete="CASCADE"))
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

    band_list = db.relationship('BandModel', uselist=False, backref='band_profile_list')
    """
        * db.relationship: para criação de relacionamentos
        * 'BandModel': indicando a model (nome da classe) que irá se relacionar
        * backref='band_profile_list': indicando qual tipo de relação está sendo feita
        * uselist=False: indicando que é uma relação de 1:1, por padrão ele vem como 'True'
    """