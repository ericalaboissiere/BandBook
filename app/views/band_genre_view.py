from flask import Blueprint, request, current_app
"""
    * Blueprint: para fazer a criação das nossas rotas
    * request: para capturar a requisição do usuário
    * current_app: para pegarmos a sessão do nosso db local
"""
from http import HTTPStatus
from app.models.band_genre_model import BandGenreModel
from app.models.band_model import BandModel
from app.models.genre_model import GenreModel


bp_band_genre = Blueprint("bp_band_genre", __name__, url_prefix="/api")
"""
    * 'bp_genre': Aqui estamos nomeando o nosso blueprint, 
    esse é o nome que irá aparecer quando rodamos 'flask routes' no terminal
    * __name__: Aqui estamos passando aonde esse blueprint está sendo definido
    * url_prefix='/api': Aqui estamos definindo qual vai ser o prefixo da nossa rota
"""


@bp_band_genre.route('/band_genre', methods=["POST"])
def band_genre():
    session = current_app.db.session
    """ 
        Variável criada para pegarmos a sessão do nosso db 
        (que foi definido no nosso app/__init__ settando app.db=db)
    """
    data = request.get_json()
    band_genre = BandGenreModel(
        band_id=data['band_id'], genre_id=data['genre_id'])  # Fazendo a criação da nossa model

    # Adicionando essa model a o nossa tabela 'band_genres'
    session.add(band_genre)
    session.commit()  # Dando commit nas inserções feita na nossa tabela

    band = BandModel.query.filter_by(id=band_genre.band_id).first()
    """
        * BandModel.query: aqui estamos começando nossa query
        * .filter_by(id=band_genre.band_id): aqui estamos fazendo a filtragem por id
        * .first(): e por fim, estamos pegando o primeiro resultado desse nosso filter
    """
    genre = GenreModel.query.filter_by(id=band_genre.genre_id).first()

    return {
        "id": band_genre.id,
        "band": band.name,
        "genre": genre.name
    }, HTTPStatus.CREATED
    """
        OBS: só conseguimos pegar 'band_genre.id' porque commitamos as inserções feitas
        no nosso banco de dados, caso você não coloque o 'session.commit()' você NÃO
        irá conseguir pegar o id.  
    """
