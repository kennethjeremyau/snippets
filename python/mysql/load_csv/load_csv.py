#!/usr/bin/env python

import MySQLdb

MYSQL_HOST = 'localhost'
MYSQL_USER = 'root'
MYSQL_PASSWORD = ''
MYSQL_DB = 'experiments'
MYSQL_TABLE = 'load_csv'

PATH = 'input.csv'

db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DB)
sql = 'LOAD DATA LOCAL INFILE \'{}\' IGNORE INTO TABLE {} LINES TERMINATED BY \'\\n\' (col1)'.format(PATH, MYSQL_TABLE)
cursor = db.cursor()
cursor.execute(sql)
db.commit()
db.close()
