from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config) #config에서정의한대로 변수설정
    
    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    from .views import main_views
    app.register_blueprint(main_views.bp)

    return app