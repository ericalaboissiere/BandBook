from flask import Blueprint, request, current_app
"""
    * Blueprint: para fazer a criação das nossas rotas
    * request: para capturar a requisição do usuário
    * current_app: para pegarmos a sessão do nosso db local
"""

from http import HTTPStatus
from app.models.band_profile_model import BandProfileModel
from app.serializers.band_profile_serializer import BandProfileSerializer


bp_band_profile = Blueprint("bp_band_profile", __name__, url_prefix="/api")
"""
    * 'bp_band_profile': Aqui estamos nomeando o nosso blueprint,
    esse é o nome que irá aparecer quando rodamos 'flask routes' no terminal
    * __name__: Aqui estamos passando aonde esse blueprint está sendo definido
    * url_prefix='/api': Aqui estamos definindo qual vai ser o prefixo da nossa rota
"""


@bp_band_profile.route('/band_profile', methods=['POST'])
def band_profile():
    session = current_app.db.session

    data = request.get_json()
    profile = BandProfileModel(
        state=data["state"],
        country=data["country"],
        ein=data["ein"],
        band_id=data["band_id"],
    )
    """
        Fazendo a inserção dos dados que vem do request à nossa tabela perfils
    """

    session.add(profile)
    session.commit()

    serializer = BandProfileSerializer(data['band_id'])

    """
        OBS: Só conseguimos utilizar esse serializer por que fizemos 'session.add(perfil)' e o 'session.commit()'
        se não tivessemos feito isso não iriamos conseguir pegar o 'perfil.id' dentro do nosso serializer
    """

    return serializer, HTTPStatus.CREATED
