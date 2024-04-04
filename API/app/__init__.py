from flask import Flask
from app.config.config import client 


def create_app():
    app = Flask(__name__)
    # Configuraciones adicionales pueden ir aquí

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
