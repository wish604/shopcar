#!C:\Users\a0983\AppData\Local\Programs\Python\Python310\python.exe
#import mariadb
import mysql.connector

try:
 	#conn = mariadb.connect(
	conn = mysql.connector.connect(
		#要連接資料庫的資訊
		user="root",
		password="",
		host="localhost",
		port=3306,
		database="shopcar"
	)
except: #mariadb.Error as e:
	print("Error connecting to DB")
	exit(1)
cur=conn.cursor()