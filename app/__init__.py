from flask import Flask
from os import getenv
from app.configurations import database, migrations
from app import views

# Importamos os dois arquivos de configuração


def create_app():
    app = Flask(__name__)

    app.config["SQLALCHEMY_DATABASE_URI"] = getenv("SQLALCHEMY_DATABASE_URI")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["JSON_SORT_KEYS"] = False

    database.init_app(app)
    migrations.init_app(app)
    views.init_app(app)
    """
        Inicializamos as configurações do nosso db e da nossa migration, que agora estão prontas para uso
    """

    return app
