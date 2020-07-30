
from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask_login import LoginManager, login_user, logout_user, login_required
from  database import db
from model import CreateFlask
from form.login_form import LoginForm
from model import login_manager
from model.models import User

app = Flask(__name__)
app.config.from_pyfile('configs.py')
Bootstrap(app)
db.init_app(app)

#login management
login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

#app = CreateFlask()

# 第二次登陆时调用 验证是否之前登陆过 返回登陆的username即可
# user loader
@login_manager.user_loader
def load_user(username):
    if User.query.get(username) is not None:
        return User.query.get(username)


# 登陆必须 装饰器
# home page
@app.route('/')
@login_required
def index():
    return render_template('index.html')

@app.route('/login', methods = ['GET', 'POST'])
def login():
    if request.method == 'POST':
        form =LoginForm()
        username = form.userid.data
        password = form.password.data

        # 表单中的账号密码 匹配查出来的账号密码 第一项 返回给user
        user = User.query.filter(form.userid.data == User.username, form.password.data == User.password).first()

        # remember ==True 关闭浏览器cookie依然有效 否则反之
        if user:
            login_user(user, remember=True)
            print("登录成功")
            return render_template("index.html")
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return 'Logout successfully.'


if __name__ == '__main__':
    app.run()
