from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    from app.routes import bp as main_bp
    app.register_blueprint(main_bp)

    with app.app_context():
        # Importing models here if necessary
        # from app import models  # Uncomment and adjust as needed

        # Create database tables (if needed)
        # db.create_all()  # Avoid calling create_all() in production

        return app
