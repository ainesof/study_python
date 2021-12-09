from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from . import models

    # 블루프린트
    from .views import main_views, question_view
    app.register_blueprint(main_views.bp)
    app.register_blueprint(main_views.err)
    app.register_blueprint(question_view.bp)
    return app





# https://www.jetbrains.com/help/pycharm/에서 PyCharm 도움말 참조
# --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org
# flask run
# 현재 시점 리비전과 최종 리비전이 같아야 migrate가 됨 https://programmer-ririhan.tistory.com/222
# https://wikidocs.net/81046