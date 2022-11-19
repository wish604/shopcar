#!C:\Users\a0983\AppData\Local\Programs\Python\Python310\python.exe
from dbconfig import conn,cur
#商品
def get():
    #查詢
    sql="select ID, name,price,num from car where num>0 order by num desc;"
    cur.execute(sql)
    records = cur.fetchall()
    return records
#添加商品到購物車
def addproduct(ID):
    if exist(ID) == []:
        sql = "select ID,name,price from product where id = %s;"
        cur.execute(sql,(ID,))
        records = cur.fetchall()
        ID = records[0][0]
        name = records[0][1]
        price = records[0][2]
        sql2="insert into car (ID,name,price,num) values (%s,%s,%s,1);"
        cur.execute(sql2,(ID,name,price))
        conn.commit()
    else:
        sql="update car set num=num+1 where ID=%s;"
        cur.execute(sql,(ID,))
        conn.commit()
    return True
#判斷商品在購物車上
def exist(ID):
    sql = "select ID,price from car where ID = %s;"
    cur.execute(sql,(ID,))
    records = cur.fetchall()
    return records
#刪除一個商品
def delproduct(ID):
    sql="update car set num=num-1 where ID=%s;"
    cur.execute(sql,(ID,))
    conn.commit()
    return True
#刪除整個商品
def delproduct2(ID):
    sql="update car set num=0 where ID=%s;"
    cur.execute(sql,(ID,))
    #提交至SQL
    conn.commit()
    return True
#結帳
def final():
    money = 0
    finals = []
    sql = "select ID, name,price, num from car where num>0;"
    cur.execute(sql)
    lists = cur.fetchall()
    #使用append函數創建列表
    for list in lists:
        pos = []
        #商品*數量=最後價格
        money =money+ list[2] * list[3]
        pos.append(list[0])
        pos.append(list[3])
        finals.append(pos)
    sql2 = "Delete from car;"
    cur.execute(sql2)
    #提交至SQL
    conn.commit()
    return money,finals
