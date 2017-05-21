#!/usr/bin/python
#-*- coding:UTF-8 -*-
from flask import Flask,request,redirect,render_template

from flaskext.mysql import MySQL

from OMS_Log import log4oms

mysql = MySQL()
app = Flask(__name__)
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '12345678'
app.config['MYSQL_DATABASE_DB'] = 'oms'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306
mysql.init_app(app)

@app.route('/mysql')
def mysql1():
    # （获得一个数据库操作游标）Obtain a cursor
    # cursor = mysql.get_db().cursor()
    cursor = mysql.get_db().cursor()
    cursor.execute("SELECT * FROM user")
    #data = cursor.fetchone()
    data = cursor.fetchall()
    if data is None:
        print 'OMS查询MySQL oms_user表出错！'
    else:

        log4oms.info('OMS查询MySQL oms_user表 结果')
        print 'OMS查询MySQL oms_user表 结果：',data[0]
        print '查询结果第一行第一列数据：',data[0][0]
        print '查询出的用户名为：',data[0][1]
        print '查询出的密码为：', data[0][2]
    return render_template('test.html')

# @app.route('/')
# def hello_world():
#     return 'Hello World!'

@app.route('/')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/main')
def main():
    return render_template('main.html')

@app.route('/main2')
def main2():
    return render_template('main2.html')



if __name__ == '__main__':
    app.run()
