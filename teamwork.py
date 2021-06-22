## import libraries
from app import create_app
from app.models.registered import Registered
from flask import Flask, Blueprint
from flask_login import LoginManager, login_required, login_user, logout_user, UserMixin

app = create_app()

app.secret_key = 's3cr3t'
login_manager = LoginManager(app)

@login_manager.user_loader
def load_user(ID_num):
    user= Registered(ID_num)
    return user

if __name__ == '__main__':
    # 启动应用服务器, 使用默认参数, 开启调试模式
    app.run(debug=True,host='127.0.0.1', port=5000)
    # app.run(host='0.0.0.0', port=5001)

