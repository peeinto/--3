#!/usr/bin/python3
#-*- coding: utf-8 -*-
l = ["牛肉","牛腩","猪杂","牛肉丸"]
l2 = ["面","米粉","河粉","桂林米粉"]
l3 = ["加煎蛋","不加煎蛋"]
foot=[]

def randomoder():#"随机器"
    import random
    foot.append(random.sample(l,1))
    foot.append(random.sample(l2,1))
    foot.append(random.sample(l3,1))

def Wdata():#"新建读取覆盖"
    f = open("01te.txt","w+")
    for i in foot:
        i = str(i).strip("[").strip("]").replace("'","").replace("'","")
        f.write(i)
    f.close

def yulan():#预览器
    f = open("01te.txt","r+")
    line = f.readline()
    print(line)
    print("\n")

def starapp():#"软件主体"
    randomoder()
    Wdata()
    yulan()

    temp = int(input("输入【1】确认并存储，【2】不喜欢重新选择:"))
    if temp == 1:
           print("结束")

    if temp == 2:
        print("\n")
        print("**************************************************")
        print("\n")
        foot.clear()
        starapp()

print("**********************开始随机*****************************")
starapp()
