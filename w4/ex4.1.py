import os
price = [50,90,150,300,500,1000]
garena = [70,135,225,450,750,1500]
goods = [0,0,0,0,0,0]
def product():
    print("       รายการสินค้า\n",20*"-")
    for i in range(6):
        print(i+1,".การีนาเชลล์ ",garena[i]," Shells ราคา ",price[i],"บาท")

def choose():
    for i in range(6):
        print(i+1,".การีนาเชลล์ ",garena[i]," Shells")
    data1 = int(input("กรุณาเลือกหยิบสินค้าหมายเลข :"))
    for i in range(6):
        if data1 == i+1:
            goods[i] +=1

def show():
    sumn = 0
    sumra = 0
    print("     ______สินค้าที่คุณหยิบมีดังนี้______\n---สินค้า",17*"-"+" จำนวน",10*"-"+"ราคา---")
    for i in range(6):
        sumn = sumn+goods[i]
        sumra = sumra+(goods[i]*price[i])
        if goods[i] > 0:
            print("การีนาเชลล์",garena[i],"Shells",6*"-",goods[i],12*"-",goods[i]*price[i])
    print("รวม",23*"-",sumn,12*"-",sumra)

while(True):
    print("   โปรแกรมเติมเกมออนไลน์   \n",25*"-")
    print("1. แสดงรายการสินค้า\n2. หยิบสินค้าเข้าตะกร้า\n3. จำนวนและราคาสินค้าที่หยิบ\n4. ปิดโปรแกรม\n")
    data = int(input("กรุณาเลือกทำรายการ :"))
    if data == 1:
        os.system('cls')
        print("กรุณาเลือกทำรายการ :"+str(data))
        product()
    elif data == 2:
        os.system('cls')
        print("กรุณาเลือกทำรายการ :"+str(data))
        choose()
    elif data == 3:
        os.system('cls')
        print("กรุณาเลือกทำรายการ :"+str(data))
        show()
    else:
        os.system('cls')
        print("กรุณาเลือกทำรายการ :"+str(data))
        out = input("คุณต้องการออกจากโปรแกรมใช่ไม(y / n) :")
        if out == 'y':
            print("ขอบคุณที่ใช้บริการ")
            break