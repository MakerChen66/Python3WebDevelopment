'''
#!/usr/bin/env python3
- * - coding=utf-8 - * -
@author     :  makerchen
@time       :  2019-5-8
@IDE        :  PyCharm/Sublime Text
@微信公众号 ：小鸿星空科技
- * - coding=utf-8 - * -
'''


import pymysql
from config import *


class MySQLClient(object):
	def __init__(self,host=MYSQL_HOST,user=MYSQL_USER,password=MYSQL_PASSWORD,port=MYSQL_PORT,db=MYSQL_DB):
		self.db = pymysql.connect(host=host,user=user,password=password,port=port,db=db)

	def update_data_or_insert_data(self,student_id,geography,chemistry,IT,history,biology,mathematics,
									general_technique,physics,english,chinese,politics):
		data = {
			'id':student_id,
			'geography':geography,
			'chemistry':chemistry,
			'IT':IT,
			'history':history,
			'biology':biology,
			'mathematics': mathematics,
			'general_technique':general_technique,
			'physics':physics,
			'english':english,
			'chinese':chinese,
			'politics':politics
		}
		table = 'information_of_grade'
		keys = ','.join(data.keys())
		values = ','.join(['%s'] * len(data))
		self.cursor = self.db.cursor()
		sql = f'insert into {table}({keys}) values({values}) on duplicate key update'
		update = ','.join([f' {key} = %s' for key in data])
		sql += update
		try:
			if self.cursor.execute(sql,tuple(data.values())*2):
				print('Successfully!')
				self.db.commit()
		except Exception as e:
			print(e.args)
			self.db.rollback()
		self.db.close()

	def delete_mysql_data(self,student_id):
		table = 'information_of_grade'
		condition = f'id = {student_id}'
		self.cursor = self.db.cursor()
		sql = f'delete from {table} where {condition}'
		try:
			if self.cursor.execute(sql):
				print('Delete Successfully!')
				self.db.commit()
		except Exception as e:
			print(e.args)
		self.db.close()

	def get_student_data(self,student_id):
		table = 'information_of_grade'
		condition = f'id = {student_id}'
		self.cursor = self.db.cursor()
		sql = f'select * from {table} where {condition}'
		try:
			if self.cursor.execute(sql):
				results = self.cursor.fetchone()	#元组返回
				student_grade = []
				[student_grade.append(result) for result in results]
				# print(student_grade)
				return student_grade

		except Exception as e:
			print(e.args)


if __name__ == '__main__':
	mysqlclient = MySQLClient()
	mysqlclient.get_student_data('194023011173')
