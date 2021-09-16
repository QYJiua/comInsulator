from flask import Flask
from settings import DevelopmentConfig
from exts import db
from flask_bootstrap import Bootstrap
from apps.insulator.views import insulator_bp
# from apps.user.views import user_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelopmentConfig)
    db.init_app(app=app)
    Bootstrap(app)
    app.register_blueprint(insulator_bp)
    # app.register_blueprint(article_bp)

    return app