#!C:\Users\a0983\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs,sys
import cgi#提供同客戶端HTML頁面的接口
import product#資料庫裡的product
from dbconfig import conn, cur

print ("Content-type:text/html;charset=utf-8\n")
sql="select ID,name,price, num from product"
cur.execute(sql)#執行sql指令
sys.stdout.flush()#緩衝區資料
product_list= finals=cur.fetchall()#拿出finals裡的資料
msg= ""#空物件
for(ID,name,price,num) in product_list:#把資料庫讀入裡面
    msg +=f"<tr ><td>編號 : {ID}</td> <td>商品 : {name}</td> <td>商品價格 : {price}</td> <td>數量 : {num}</td> </tr>" 
    #檔案讀取/寫入
with open("manage.html","rb") as file:
    st=file.read()
    st=st.replace(b"msg",msg.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()