#!C:\Users\a0983\AppData\Local\Programs\Python\Python310\python.exe
#-*- coding: utf-8 -*-
#處理stdio輸出編碼，以避免亂碼
import codecs,sys
import cgi
import product
import car

sys.stdout=codecs.getwriter('utf-8')(sys.stdout.buffer)

#先印出http 表頭
print("Content-Type: text/html; charset=utf-8\n")
print("""
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>checkout</title>
</head>
<style type="text/css">
        body {
            padding:0;
            margin:0;
            width:100%;
            height:100vh;
            background:#b7ebff;
        }
        .container {
            width: 200px;
            height: 60px;
            position: absolute;
            left:50%;
            top: 50%;
            transform: translate(-50%, -50%);
        }
        .circle{
            width:20px;
            height:20px;
            position: absolute;
            border-radius: 50%;
            background-color: #4aa2fb;
            left:15%;
            transform-origin: 50%;
            animation:circle .5s alternate infinite ease;
        }
        @keyframes circle {
            0%{
                top:60px;
                height:5px;
                border-radius:50px 50px 25px 25px;
                transform: scaleX(1.7);
            }
            40%{
                height:20px;
                border-radius: 50%;
                transform: scaleX(1);
            }
            100%{
                top:0%;
            }
        }
        .circle:nth-child(2){
            left:45%;
            animation-delay: .2s;
        }
        .circle:nth-child(3){
            left:auto;
            right:15%;
            animation-delay: .3s;
        }
        .shadow{
            width:20px;
            height:4px;
            border-radius:50%;
            background-color: rgba(2, 33, 100, 0.5);
            position:absolute;
            top:62px;
            transform-origin: 50%;
            z-index: -1;
            left:15%;
            filter: blur(1px);
            animation:shadow .5s alternate infinite ease;
        }
        @keyframes shadow {
            0%{
                transform: scaleX(1.5);
            }
            40%{
                transform:scaleX(1);
                opacity: .7;
            }
            100%{
                transform: scaleX(.2);
                opacity: .4;
            }
        }
        .shadow:nth-child(4){
            left:45%;
            animation-delay: .2s;
        }
        shadow:nth-child(5){
            left:auto;
            right:15%;
            animation-delay: .3s;
        }
    </style>
<body>
    <div class="container">
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="circle"></div>
        <div class="shadow"></div>
        <div class="shadow"></div>
        <div class="shadow"></div>
    </div>
""")

finals =[]
money,finals =car.final()
product.final(finals)#減少庫存
if(money >1000):
    print("<div align='center'#text='center' style='text-align: center;font-weight:bold;'>總共消費:</div>",money-100)
else:
    print("<div align='center'#text='center' style='text-align: center;font-weight:bold;'>總共消費:</div>",money)
print("<div style='text-align: center ;color:#BF0060; size:150;font-weight:bold;'>感謝您的消費!!!</div>")
print("<div style='text-align: center;'><br><meta http-equiv='refresh' content='5;url=http://localhost/shopcar/shop.py'></div>")
print("</body></html>")

