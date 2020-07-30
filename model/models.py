
from flask_login import UserMixin
from database import db

class User(db.Model, UserMixin):
    username = db.Column('username', db.String(64), primary_key=True)
    password = db.Column('password', db.String(64))

    __tablename__='userinfo'

    def __init__(self,username=None , password =None):
        self.username=username
        self.password=password

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.username)

    #自定义print此对象时打印的内容
    def __repr__(self):
        return '<User %r>' % (self.username)
