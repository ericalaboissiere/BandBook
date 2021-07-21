from flask import Blueprint, request, current_app
"""
    * Blueprint: para fazer a criação das nossas rotas
    * request: para capturar a requisição do usuário
    * current_app: para pegarmos a sessão do nosso db local
"""

from http import HTTPStatus
from app.models.album_model import AlbumModel
from app.models.band_model import BandModel
import ipdb


bp_album = Blueprint("bp_album", __name__, url_prefix="/api")


@bp_album.route("/album", methods=["POST"])
def album():
    session = current_app.db.session

    data = request.get_json()
    album = AlbumModel(
        name=data["name"], band_id=data["band_id"], release_year=data["release_year"])
    """
        Pegamos a albumModel para termos os dados da albuma a ser adicionada o band_id de referencia
    """

    band = BandModel.query.get(data["band_id"])
    """
        Pegamos a BandModel para podermos identificar no return o nome da banda a que aquela albuma foi adicionada
    """
    music_list = album.music_list
    ipdb.set_trace()
    session.add(album)
    session.commit()

    return {
        "id": album.id,
        "album_name": album.name,
        "release_year": album.release_year,
        "band_name": band.name,
        "musics": [music.name for music in music_list],

    }, HTTPStatus.CREATED
