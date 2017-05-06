#!/usr/bin/python
#-*- coding:UTF-8 -*-
from flask import Flask
import MySQLdb
from flask.ext.sqlalchemy import  SQLAlchemy

# 查询数据库
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@localhost/oms'
db = SQLAlchemy(app)

#class User(db.Model):