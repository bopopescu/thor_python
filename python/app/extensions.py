# 作者: thor
# 时间: 2019/4/27 4:14
# 文件名: extensions
# 介绍: 扩展文件，加载项目需要的package


# pymysql 应用
# import pymysql
#
# conn = pymysql.connect(host='127.0.0.1', user='root', password='yuefei12', db='thor_python')
# cur = conn.cursor(cursor=pymysql.cursors.DictCursor)
# recount = cur.execute("SELECT * FROM `test`;")
# print(cur.fetchall())

# sqlalchemy简单应用
# from sqlalchemy import Column, String, create_engine
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.ext.declarative import declarative_base
#
# Base = declarative_base()
#
# class Text(Base):
#     # 表名字
#     __tablename__ = 'test'
#
#     # 表结构
#     id = Column(String(2), primary_key=True)
#     title = Column(String(255))
#     content = Column(String(255))
#     time = Column(String(255))
#     biaoti = Column(String(255))
#     ceshi = Column(String(255))
#     data = Column(String(255))
#     pass
#
# engine = create_engine("mysql+pymysql://root:yuefei12@127.0.0.1:3306/thor_python")
# DBSession = sessionmaker(bind=engine)
# session = DBSession()
# test = session.query(Text).filter(Text.id>=1).all()
# for t in test:
#     print(t.content)
#
# session.close()


# flask-sqlalchemy+sqlalchemy
# from flask_sqlalchemy import SQLAlchemy
# import pymysql
# from flask import Flask
#
# app = Flask(__name__)
#
# app.config['SECRET_KEY'] = 'thor is reading book!'
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:yuefei12@127.0.0.1:3306/thor_python'
# app.config['SQLALCHEMY_COMMT_ON_TEARDOWN'] = True
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
#
# db = SQLAlchemy(app)

# class Test(db.Model):
#     __tablename__ = 'test'
#     id = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(255))
#     content = db.Column(db.String(255))
#     time = db.Column(db.String(255))
#     biaoti = db.Column(db.String(255))
#     ceshi = db.Column(db.String(255))
#     data = db.Column(db.String(255))

    # def __init__(self, id, title, content, time, biaoti, ceshi, data):
    #     self.id = id
    #     self.title = title
    #     self.content = content
    #     self.time = time
    #     self.biaoti = biaoti
    #     self.ceshi = ceshi
    #     self.data = data

#     def __repr__(self):
#         return '%s %s %s %s %s %s %s' % (self.id, self.title, self.content, self.time, self.biaoti, self.ceshi, self.data)
#         datas = {
#             'id': self.id,
#             'title': self.title,
#             'content': self.content,
#             'time': self.time,
#             'biaoti': self.biaoti,
#             'ceshi': self.ceshi,
#             'data': self.data
#         }
#         return datas
#         pass
#
# data = Test.query.all()
# print(data)