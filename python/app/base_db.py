# -*- coding: utf-8 -*-
# 作者: thor
# 时间: 2019/4/30 15:35
# 文件名: base_db
# 介绍:

import pymysql
from config import Config

class DBBaseClass:
    __tablename__ = 'users'
    __fillable__ = []
    __hidden__ = []

    def __init__(self):
        # 初始化数据库
        self.connect = pymysql.connect(
            host=Config.DB_HOST or '127.0.0.1',
            user=Config.DB_USER or 'root',
            passwd=Config.DB_PASS or 'root',
            db=Config.DB_DATABASE or 'test',
            port=Config.DB_PORT or 3306,
            charset=Config.CHARSET or 'utf8'
        )
        self.cursor = self.connect.cursor(cursor=pymysql.cursors.DictCursor)

    # 查找一条消息
    def find(self, values):
        sql = "SELECT %s FROM `%s` WHERE id='%s';" % (self.get_fillable(), self.__tablename__, values)
        return self.cursor.fetchone() if self.execute(sql) else 'no data!'

    # 查找多条数据
    def where(self, values, operator='and'):
        # 遍历values组合条件
        if isinstance(values, dict):
            sql = ''
            for value in values:
                sql += """%s='%s' %s """ % (value, values[value], operator)
            sql = "SELECT %s FROM `%s` WHERE %s;" % (self.get_fillable(), self.__tablename__, sql[:-(len(operator)+2)])
            return self.cursor.fetchall() if self.execute(sql) else 'no data!'
        else:
            return '参数需要是dict类型'

    # 单条添加
    def add(self, values):
        string, lists = '', []
        for value in values:
            string += "%s," % value
            lists.append(values[value])
        sql = "INSERT INTO `%s` (%s) VALUES " % (self.__tablename__, string[:-1]) + "(" + (("%s," * len(lists))[:-1] + ");")
        self.execute(sql, lists)
        return self.cursor.lastrowid

    # 单条修改
    def update(self, values, operator):
        sql = ''
        for value in values:
            sql += "%s='%s'," % (value, values[value])
        sql = "UPDATE `%s` SET %s WHERE %s;"  % (self.__tablename__, sql[:-1], operator)
        return self.execute(sql)

    # 执行sql语句

    # 删除语句
    def delete(self, operator):
        return self.cursor(operator)

    def execute(self, string, params=None, operator='execute'):
        if operator == 'execute':
            if params:
                results = self.cursor.execute(string, params)
            else:
                results = self.cursor.execute(string)
        elif operator == 'executemany':
            if params:
                results = self.cursor.executemany(string, params)
            else:
                results = self.cursor.executemany(string)
        self.connect.commit()
        return results

    # 按要求获取表所有字段
    def get_fillable(self, operator=True):
        fillable = [i for i in self.__fillable__ if i not in self.__hidden__]
        if operator:
            results = ', '.join(fillable)
        else:
            results = (', '.join(fillable))[4:]
        return results

    # 关闭数据库与游标
    def __del__(self):
        self.cursor.close()
        self.connect.close()

class Article(DBBaseClass):
    __tablename__ = 'article'
    __fillable__ = [
        'id', 'title', 'content', 'time'
    ]
    __hidden__ = [

    ]

article = Article()
# formData = dict(
#     id=1,
#     title='改成sql'
# )
# print(article.find(10))
# print(article.where(formData, 'OR'))
# add_data = (
#     ('测试数据标题11123', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》11123'),
#     ('测试数据标题11123', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》11123'),
#     ('测试数据标题11123', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》11123'),
#     ('测试数据标题11123', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》11123'),
#     ('测试数据标题11123', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》11123'),
#     ('测试数据标题11123', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》11123')
# )
data = dict(
    time="测试时间",
    content="测试数",
    title="测试数据标题11123"
)
# print(article.add(data))
print(article.update(data, "id=1"))