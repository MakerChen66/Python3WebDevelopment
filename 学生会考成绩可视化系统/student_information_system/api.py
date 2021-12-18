'''
#!/usr/bin/env python3
- * - coding=utf-8 - * -
@author     :  makerchen
@time       :  2019-5-8
@IDE        :  PyCharm/Sublime Text
@微信公众号 ：小鸿星空科技
- * - coding=utf-8 - * -
'''


from flask import Flask,g,render_template,request
from mysql_db import MySQLClient
from config import *


__all__ = ['app']
app = Flask(__name__)


def get_conn():
	if not hasattr(g,'mysql'):
		g.mysql = MySQLClient()
	return g.mysql

@app.route('/index')
def index():
	return render_template('home_index.html')

@app.route('/student/<kaosheng_number>')
def get_grade(kaosheng_number):
	mysqlclient = MySQLClient()
	student_grade = mysqlclient.get_student_data(str(kaosheng_number))
	kaosheng_number = student_grade[0]
	geography = student_grade[1]
	chemistry = student_grade[2]
	IT = student_grade[3]
	history = student_grade[4]
	biology = student_grade[5]
	mathematics = student_grade[6]
	general_technique = student_grade[7]
	physics = student_grade[8]
	english = student_grade[9]
	chinese = student_grade[10]
	politics = student_grade[11]

	return render_template('grade.html',kaosheng_number=kaosheng_number,geography=geography,chemistry=chemistry,IT=IT,
							history=history,biology=biology,mathematics=mathematics,
							general_technique=general_technique,physics=physics,english=english,
							chinese=chinese,politics=politics
							)


if __name__ == '__main__':
	app.run(API_HOST,API_PORT)