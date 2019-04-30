# 作者: thor
# 时间: 2019/4/27 3:48
# 文件名: __init__
# 介绍:

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app(config_class=None):
    app = Flask(__name__)

    return app
