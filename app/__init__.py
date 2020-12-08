from flask import Flask
from flask_wtf import CSRFProtect

from app.auth.models import User
from app.auth.views import auth
from app.db import db, ma
from conf.config import DevelopmentConfig
from app.products.views import products
from flask_migrate import Migrate
from flask_login import LoginManager

ACTIVE_ENDPOINTS = [("/products", products), ("", auth)]


def create_app(config=DevelopmentConfig):
    app = Flask(__name__)
    migrate = Migrate(app, db)
    csrf = CSRFProtect(app)
    app.config.from_object(config)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'

    login_manager.init_app(app)
    db.init_app(app)
    ma.init_app(app)
    csrf.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        db.create_all()

    # register each active blueprint
    for url, blueprint in ACTIVE_ENDPOINTS:
        app.register_blueprint(blueprint, url_prefix=url)

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table,
        # use it in
        # the query for the user
        return User.query.get(int(user_id))

    return app


if __name__ == "__main__":
    app_flask = create_app()
    app_flask.run()
