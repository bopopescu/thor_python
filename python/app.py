# * coding=utf-8 *
# 作者: Ant
# 时间: 2019/4/14 2:13
# 文件名: app
# 介绍:

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return "Hello Python!!!"

