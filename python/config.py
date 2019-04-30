# 作者: thor
# 时间: 2019/4/27 2:16
# 文件名: config
# 介绍:

import os
from hashlib import md5
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__)) # 根目录
dotenv_path = os.path.join(os.path.abspath(os.path.dirname(__file__)), '.env') # .env路径

if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path, override=True)  #  override=True: 覆写已存在的变量

get_env = os.environ.get # .env 属性

class Config:
    APP_NAME = get_env('APP_NAME') or 'default' # 项目名称
    SECRET_KEY = md5('{0}'.format(get_env('APP_NAME') or 'thor is reading book').encode('utf-8')).hexdigest() # 项目密匙

    CHARSET = get_env('CHARSET')

    # 数据库属性
    DB_CONNECTION = get_env("DB_CONNECTION")
    DB_DATABASE = get_env("DB_DATABASE")
    DB_HOST = get_env("DB_HOST")
    DB_USER = get_env("DB_USER")
    DB_PASS = get_env("DB_PASS")
    DB_PORT = int(get_env("DB_PORT"))
