#! /usr/bin/env python
# coding=utf-8

import pymysql
import sys

def execute(sql):
	try:
		cursor.execute(sql) #每次只能执行一条语句
		db.commit()
	except Exception as err:
		db.rollback()
		print(sql)
		print(repr(err))
		sys.exit()

ip = "localhost"
user = "python"
password = "python"
db_name = "python"
db = pymysql.connect(ip, user, password, db_name)
cursor = db.cursor()

cursor.execute("SELECT VERSION()")
print("database version:", cursor.fetchone())

execute("DROP TABLE IF EXISTS employee;")
sql = \
"""
CREATE TABLE employee(
	first_name CHAR(20) NOT NULL,
	last_name CHAR(20),
	age INT,
	sex char(1),
	income FLOAT
);
"""
execute(sql)

sql = \
"""
INSERT INTO employee(first_name, last_name, age, sex, income)
VALUES("Mac", "Mohan", 20, "M", 2000);
"""
execute(sql)

sql = \
"""
INSERT INTO employee(first_name, last_name, age, sex, income)
VALUES("Justin", "King", 23, "M", 500);
"""
execute(sql)

sql = \
"""
SELECT * FROM employee WHERE income < 1000;
"""
execute(sql)
print("rowcount:", cursor.rowcount)
print("fetchone:", cursor.fetchone())

execute("SELECT * FROM employee WHERE income > 100;")
results = cursor.fetchall()
print("fetchall:", results)
for row in results:
	print("first_name:{0}, last_name:{1}, age:{2}, sex:{3}, income:{4}"
		.format(row[0], row[1], row[2], row[3], row[4]))

db.close()