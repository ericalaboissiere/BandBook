from flask import Blueprint, request, current_app
"""
    * Blueprint: para fazer a criação das nossas rotas
    * request: para capturar a requisição do usuário
    * current_app: para pegarmos a sessão do nosso db local
"""

from http import HTTPStatus
from app.models.music_model import MusicModel
from app.models.band_model import BandModel

bp_music = Blueprint("bp_music", __name__, url_prefix="/api")


@bp_music.route("/music", methods=["POST"])
def music():
    session = current_app.db.session

    data = request.get_json()
    music = MusicModel(name=data["name"], band_id=data["band_id"])
    """
        Pegamos a MusicModel para termos os dados da musica a ser adicionada o band_id de referencia
    """

    band = BandModel.query.get(data["band_id"])
    """
        Pegamos a BandModel para podermos identificar no return o nome da banda a que aquela musica foi adicionada
    """

    session.add(music)
    session.commit()

    return {
        "id": music.id,
        "music_name": music.name,
        "band_name": band.name,
    }, HTTPStatus.CREATED
