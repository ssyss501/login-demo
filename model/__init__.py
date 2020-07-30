from flask import Flask
import configs
from flask_bootstrap import Bootstrap
from database import db
from flask_login import LoginManager

login_manager = LoginManager()
login_manager.login_view = 'login'


#初始化
def CreateFlask():
    app = Flask(__name__)
    login_manager.init_app(app)
    app.config.from_pyfile('../configs.py')
    Bootstrap(app)
    db.init_app(app)
    return app