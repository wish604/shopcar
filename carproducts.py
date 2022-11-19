#!C:\Users\a0983\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs,sys
import cgi
import car#資料庫裡的car

print ("Content-type:text/html;charset=utf-8\n")

sys.stdout.flush()#緩衝區資料
car_list=car.get()#讀出資料庫的內容
msg2= ""#空物件
for(ID,name,price,num) in car_list:#把資料庫讀入裡面
    msg2 +=f"<tr ><td>編號 : {ID}</td> <td>商品 : {name}</td> <td>商品價格 : {price}</td> <td>購買數量 : {num}</td> </tr>" 
    #檔案讀取/寫入
with open("carproducts.html","rb") as file:
    st=file.read()
    st=st.replace(b"msg2",msg2.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()