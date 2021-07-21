from flask import Blueprint, request, current_app
"""
    * Blueprint: para fazer a criação das nossas rotas
    * request: para capturar a requisição do usuário
    * current_app: para pegarmos a sessão do nosso db local
"""

from http import HTTPStatus
from app.models.band_model import BandModel

from app.serializers.band_serializer import BandSerializer
"""
    Importamos nosso serializador customizado
"""

bp_band = Blueprint("bp_band", __name__, url_prefix="/api")
"""
    * 'bp_band': Aqui estamos nomeando o nosso blueprint,
    esse é o nome que irá aparecer quando rodamos 'flask routes' no terminal
    * __name__: Aqui estamos passando aonde esse blueprint está sendo definido
    * url_prefix='/api': Aqui estamos definindo qual vai ser o prefixo da nossa rota
"""


@bp_band.route('/band', methods=["POST"])
def band():
    session = current_app.db.session
    """
        Variável criada para pegarmos a sessão do nosso db
        (que foi definido no nosso app/models/__init__.py settando app.db=db)
    """

    data = request.get_json()
    band = BandModel(name=data["name"])  # Fazendo a criação da nossa model
    session.add(band)  # Adicionando essa model a o nossa tabela 'bands'
    session.commit()  # Dando commit nas inserções feita na nossa tabela

    return {"id": band.id, "band_name": band.name}, HTTPStatus.CREATED
    """
        OBS: só conseguimos pegar o 'band.id' porque commitamos as inserções feitas 
        no nosso banco de dados, caso você não coloque o 'session.commit()' você NÃO 
        irá conseguir pegar o id. 
    """


@bp_band.route('/band/<int:id>')
def get_band_by_id(id):
    serializer = BandSerializer(id)
    return serializer


"""
    * Chamamos nosso serializador passando a id da banda como parametro
    * Retornamos o nosso searializador no GET da view criada
"""
