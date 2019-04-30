# -*- coding:utf-8 -*-
# 作者: thor
# 时间: 2019/4/27 20:57
# 文件名: databases
# 介绍:

import pymysql
from config import Config

con = pymysql.connect(
    host='localhost',
    user='root',
    passwd='yuefei12',
    db='test',
    port=3306,
    charset='utf8'
)
cur = con.cursor(cursor=pymysql.cursors.DictCursor) # pymysql.cursors.DictCursor 默认是返回列表，添加这个参数返回的是字典

# execute 会返回执行sql影响的行数
# cur.execute('SELECT * FROM `article`') # 查找
# print(cur.fetchone()) # 根据条件返回一条数据
# print(cur.fetchmany(10)) # 根据需求返回一定量的数据结果
# print(cur.fetchall()) # 根据条件，返回所有数据

# con.commit()
# 添加一条数据
# params = (
#     '测试数据标题111',
#     '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》111'
# )
# cur.execute("INSERT INTO `article` (title, content) VALUES (%s, %s)", params) # 执行sql 第二个参数是插入的数据
# con.commit() # 提交

# 批量添加数据
params1 = ["测试数据标题111", "测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》111"]
params2 = [
    ['测试数据标题111', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》111'],
    ['测试数据标题1111', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1111'],
    ['测试数据标题1112', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1112'],
    ['测试数据标题1113', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1113'],
    ['测试数据标题1114', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1114'],
    ['测试数据标题111', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》111'],
    ['测试数据标题1111', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1111'],
    ['测试数据标题1112', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1112'],
    ['测试数据标题1113', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1113'],
    ['测试数据标题1114', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1114'],
]
cur.executemany("INSERT INTO `article` (title, content) VALUES (%s, %s)", params2) # 执行sql 批量添加使用 第二个参数是插入的数据
con.commit() # 提交
print(cur.lastrowid) # 获取插入自增id

# cur.close() 关闭游标
# con.close() # 关闭数据库

# class DBBaseClass:
#     conn = None # 数据库链接
#     cursor = None # 指针
#     __tablename__ = 'users' # 表名
#     __fillable__ = [ # 数据库全部字段
#
#     ]
#     __hidden__ = [ # 隐藏显示字段
#
#     ]
#
#     def __init__(self): # 初始化
#         self.connect() # 初始化数据库
#
#     def find(self, _id): # 查询一条数据
#         self.exectue(self.is_sql() + ("id='%s'" % _id))
#         data = self.cursor.fetchone()
#         self.close()
#         return data
#
#     def where(self, column, boolean='and'): # 查询所有数据
#         if isinstance(column, str):
#             sql = column
#         elif isinstance(column, dict):
#             sql = self.splicing(column, boolean)
#         return self.fetch_all(self.is_sql() + sql)
#
#     def add(self, column): # 添加数据 添加多条数据，功能尚未完善
#         self.exectue(self.is_sql('insert') + "(%s, %s)", column, typeof='executemany')
#         return self.commit()
#
#     def update(self): # 修改数据
#         ...
#
#     def delete(self): # 删除数据
#         ...
#
#     def is_fillable(self): # 返回显示表字段
#         return ', '.join([i for i in self.__fillable__ if i not in self.__hidden__])
#
#     def is_sql(self, _type='select'): # 未完成
#         fillable = self.__fillable__
#         hidden = self.__hidden__
#         tablename = self.__tablename__
#         tables = [i for i in fillable if i not in hidden]
#         tables = ', '.join(tables)
#         sql = {
#             'select': '''SELECT %s FROM `%s` WHERE ''' % (tables, tablename),
#             'insert': '''INSERT INTO `%s` (%s) VALUES ''' % (tablename, tables[4:]),
#             'update': '''UPDATE `%s` SET ''' % tablename,
#             'delete': '''DELETE FROM `%s` WHERE ''' % tablename
#         }
#
#         return sql[_type]
#
#     def exectue(self, sql, params=None, typeof='execute'): # 执行sql语句返回行数
#         dictions = dict(
#             execute=self.cursor.execute,
#             executemany=self.cursor.executemany
#         )
#         return dictions[typeof](sql, params) if params else dictions[typeof](sql)
#
#     def fetch_all(self, string): # 返回全部数据
#         self.exectue(string)
#         return self.cursor.fetchall(), self.close()
#
#     def commit(self):
#         self.conn.commit()
#         new_id = self.cursor.lastrowid
#         self.close()
#         return new_id
#
#     def commit_all(self, string):
#         self.exectue(string)
#
#
#     def connect(self): # 初始化数据库
#         self.conn = pymysql.connect(
#             host=Config.DB_HOST,
#             user=Config.DB_USER,
#             passwd=Config.DB_PASS,
#             db=Config.DB_DATABASE,
#             port=Config.DB_PORT,
#             charset=Config.CHARSET
#         )
#         self.cursor = self.conn.cursor(cursor=pymysql.cursors.DictCursor)
#
#     def close(self): # 关闭数据库
#         self.conn.close()
#         self.cursor.close()
#
#     def splicing(self, dictions, boolean): # 拼接条件
#         string = ''
#         if isinstance(dictions, dict):
#             for diction in dictions:
#                 string += "%s='%s' %s " % (diction, dictions[diction], boolean)
#             return string[:-(len(boolean)+2)]
#
# class Article(DBBaseClass):
#     __tablename__ = 'article'
#     __fillable__ = [
#         'id', 'title', 'content'
#     ]

# db = DBBaseClass()
# print(db.find(1))

# article = Article()
# add_data = (
#     ('测试数据标题111', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》111'),
#     ('测试数据标题1111', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1111'),
#     ('测试数据标题1112', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1112'),
#     ('测试数据标题1113', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1113'),
#     ('测试数据标题1114', '测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》测试数据内容》》》》》1114'),
# )
# print(article.add(add_data)) # 添加简单实现
# print(article.where("id='1' or title='sql'"))

# select 简单实现
# print(article.find(1)) 单挑数据查找
# print(article.where("id>='1' and title='sql'")) 直接写sql查找，直接写sql语句
# print(article.where(["id='%s'" % a, "title='%s'" % title, "content='%s'" % content], 'or')) 列表查找 未完成
# print(article.where({ 字典查找
#     'id': 1,
#     'title': 'sql',
#     'content': 'abcdqweasdasda'
# }, 'or'))


# class GetConnectDb(EnvConfig):
#     def __init__(self, env, db_name):
#         EnvConfig.__init__(self, env, db_name)
#         ip = self.ip
#         port = self.port
#         user = self.user
#         pwd = self.pwd
#         db = self.db_name
#         self.connect = pymysql.connect(ip, port, user, pwd, db, charset='utf8')
#         self.cursor = self.connect.cursor()
#         try:
#             if self.cursor:
#                 pass
#         except ConnectionError as e:
#             print(e)
#
#     """
#     /*
#       @:param:  sql  Usage:select * xx t_job where pipelineId='6444df4555sa55dgd';
#       @:param:  rows type is int ，get  the first  rows of data
#     */
#     """
#
#     def disconnect_db(self):
#         try:
#             self.cursor.close()
#             self.connect.close()
#         except ConnectionAbortedError as e:
#             try:
#                 self.disconnect_db()
#             except ConnectionAbortedError as e:
#                 print(e)
#             print(e)
#
#     def exe_select(self, sql, rows=None):
#         try:
#             if rows == None:
#                 try:
#                     self.cursor.execute(sql)
#                     res = self.cursor.fetchall()
#                     return res
#                 except SyntaxError as e:
#                     print(e)
#                 finally:
#                     self.disconnect_db()
#             else:
#                 try:
#                     self.cursor.execute(sql)
#                     res = self.cursor.fetchmany(rows)
#                     return res
#                 except SyntaxError as e:
#                     print(e)
#                 finally:
#                     self.disconnect_db()
#         except Exception as e:
#             print(e)
#
#     """
#     /*
#       @:param:
#       Usage:
#       when is self.execute(sql) Usage:
#           sql = insert into t_job(column1,column2,column3)values(a,b,c)
#           array=None
#       when is self.executemany(sql,array) Usage:
#             sql = insert into t_job(id,user,date）values(%s,%s,%s)
#             array = [(1001,"dev",'2018-11-25-11-12-43'),(1002,"test",'2018-11-25-11-12-44')]
#       @:param:  rows type is int ，get  the first  rows of data
#     */
#     """
#
#     def exe_insert(self, sql, array=None):
#         try:
#             if array is None:
#                 try:
#                     self.cursor.execute(sql)
#                     self.connect.commit()
#                 except SyntaxError as e:
#                     self.connect.rollback()
#                     print(e)
#                 finally:
#                     self.disconnect_db()
#             else:
#                 try:
#                     self.cursor.executemany(sql, array)
#                     self.connect.commit()
#                 except SyntaxError as e:
#                     self.connect.rollback()
#                     print(e)
#                 finally:
#                     self.disconnect_db()
#         except Exception as e:
#             print(e)
#
#     """
#     /*
#     update sql :
#     @:param: sql
#     */
#     """
#
#     def update_opt(self, sql):
#         try:
#             self.cursor.execute(sql)
#             self.connect.commit()
#         except Exception as e:
#             self.connect.rollback()
#             print(e)
#         finally:
#             self.disconnect_db()
#
#     def delete_opt(self, sql):
#         try:
#             self.cursor.execute(sql)
#             self.connect.commit()
#         except SyntaxError as e:
#             self.connect.rollback()
#             print(e)
#         finally:
#             self.disconnect_db()












