#!C:\Users\a0983\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs,sys
import cgi
import product

sys.stdout = codecs.getwriter('utf8')(sys.stdout.buffer)
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")

form = cgi.FieldStorage()#獲取資料
ID=form.getvalue('ID')
name=form.getvalue('name')
price=form.getvalue('price')
num=form.getvalue('num')
product.addproduct_m(ID,name,price,num)

