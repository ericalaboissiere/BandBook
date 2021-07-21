from flask import Blueprint, request, current_app
"""
    * Blueprint: para fazer a criação das nossas rotas
    * request: para capturar a requisição do usuário
    * current_app: para pegarmos a sessão do nosso db local
"""
from http import HTTPStatus
from app.models.genre_model import GenreModel


bp_genre = Blueprint("bp_genre", __name__, url_prefix="/api")
"""
    * 'bp_genre': Aqui estamos nomeando o nosso blueprint,
    esse é o nome que irá aparecer quando rodamos 'flask routes' no terminal
    * __name__: Aqui estamos passando aonde esse blueprint está sendo definido
    * url_prefix='/api': Aqui estamos definindo qual vai ser o prefixo da nossa rota
"""


@bp_genre.route('/genre', methods=["POST"])
def genre():
    session = current_app.db.session
    """
        Variável criada para pegarmos a sessão do nosso db
        (que foi definido no nosso app/__init__ settando app.db=db)
    """
    data = request.get_json()
    genre = GenreModel(name=data["name"])  # Fazendo a criação da nossa model
    session.add(genre)  # Adicionando essa model a o nossa tabela 'genres'
    session.commit()  # Dando commit nas inserções feita na nossa tabela

    return {"id": genre.id, "genre_name": genre.name}, HTTPStatus.CREATED

    """
        OBS: só conseguimos pegar o 'genre.id' porque commitamos as inserções feitas
        no nosso banco de dados, caso você não coloque o 'session.commit()' você NÃO
        irá conseguir pegar o id. """
