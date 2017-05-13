#!/usr/bin/python
#-*- coding:UTF-8 -*-
from flask import Flask
import MySQLdb
from flask.ext.sqlalchemy import  SQLAlchemy

# 查询数据库11
app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess'

# 这里登陆的是root用户，要填上自己的密码，MySQL的默认端口是3306，填上之前创建好的数据库名oms,连接方式参考 \
# http://docs.sqlalchemy.org/en/latest/dialects/mysql.html
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:12345678@localhost:3306/oms'

#设置这一项是每次请求结束后都会自动提交数据库中的变动
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

#实例化
db = SQLAlchemy(app)

# 定义模型，建立关系
class User(db.Model):
    # 定义表名
    __tablename__ = 'oms_user'
    # 定义列对象
    userid = db.Column(db.VARCHAR)
    username = db.Column(db.VARCHAR)
    password = db.Column(db.VARCHAR)
    logintime = db.Column(db.VARCHAR)
    rmk = db.Column(db.VARCHAR)

    def __repr__(self):
        return '<User {}>'.format(self.username)

if __name__=='__main__':
    User.query.filter_by(role=U).all()  # 注意过滤器的使用