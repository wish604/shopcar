#!C:\Users\a0983\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs,sys
import cgi
import product
#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")

#查詢
form = cgi.FieldStorage()
ID=form.getvalue('ID')
product.delete(ID)