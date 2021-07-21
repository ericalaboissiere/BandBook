from flask import Flask
# Import para typehinting

from flask_migrate import Migrate
# Import para uso da biblioteca


def init_app(app: Flask):
    Migrate(app, app.db)