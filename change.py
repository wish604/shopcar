#!C:\Users\a0983\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs,sys
import cgi
import product

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
sys.stdout.flush()
form=cgi.FieldStorage()#獲取資料
ID=form.getvalue('ID')
records=product.gets(ID)
ID=str(ID)
name = str(records[0][1])
price = str(records[0][2])
num = str(records[0][3])


with open("change.html","rb") as file:
    #str.replace(old,new[,max])
    #回傳值回傳取代後新的結果字串
    st = file.read()
    st = st.replace(b"#ID",ID.encode())
    st = st.replace(b"#name",name.encode())
    st = st.replace(b"#price",price.encode())
    st = st.replace(b"#num",num.encode())
    sys.stdout.buffer.write(st)
sys.stdout.flush()