# !C:\Users\f3245\AppData\Local\Microsoft\WindowsApps\python.exe
from dbconfig import conn, cur
def get():
    #查詢
    sql="select ID, name,price, num from product where num>0 order by num desc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
#減資料庫的數量
def final(finals):
    for final in finals:
        sql="update product set num=num-%s where ID=%s;"
        cur.execute(sql,(final[1],final[0]))
        conn.commit()
#添加商品
def addproduct_m(ID,name, price, num):
    sql="insert into product(ID,name,price,num) values (%s,%s,%s,%s);"
    cur.execute(sql,(ID,name,price,num))
    #提交至SQL
    conn.commit()
    return True
#舊資料
def gets(ID):
    sql="select ID,name,price, num from product where ID = %s"
    cur.execute(sql,(ID,))
    records = cur.fetchall()
    return records
#更改資料
def changed(ID,name,price,num):
    sql = "update product set name=%s,price=%s,num=%s where ID=%s;"
    cur.execute(sql,(name,price,num,ID))
    conn.commit()
    return True
#刪除資料
def delete(ID):
    sql="delete from product where ID=%s;"
    cur.execute(sql,(ID,))
    conn.commit()
    return True
