"""
n1=input("Input First Number\n")
n2=input("Input Second Numder\n")
print(n1," = ",n2,":",n1==n2)
print(n1," > ",n2,":",n1>n2)
print(n1," < ",n2,":",n1<n2)
a = 60
b = 13
c = 0

c = a & b
print(c)

c = a | b
print(c)

c = a ^ b
print(c)

c = ~a
print(c)

c = a << 2
print(c)

c = a >> 2
print(c)
print("Day Converter Program")
days = float(input("Input num of Days --> "))
print(days," Days --> Hour ",days*24," Hours ")
print(days," Days --> Hour ",(days*24)*60," Hours ")
print(days," Days --> Hour ",((days*24)*60)*60," Hours ")

friend = ["jan","cream","phu","bam","aom","pee","bas","kong","da","james"]
friend.append("dome")
friend.append("poonbang")
friend.insert(1,"cas")
friend.insert(7,"ped")
friend.remove("aom")
friend.pop(3)
del friend[7]
friend.clear()
del friend
print(friend)

animal = {"cat","dog","rat","pig","ant"}
animal.add("monkey")
animal.update(["python","capidara","spider","wombat","penguin","crocodile"])
print(animal)

print("++++++++++++++++++++++++++\n   โปรแกรมหยิบของใส่ตะกร้า   \n++++++++++++++++++++++++++")
a=[]
for i in range(5):
    b=input("สิ่นค้าชินที่ "+str(i+1)+"     ")
    a.append(b)
print("สินค้าของท่านคือ")
for i in range(5):
    print(i+1,a[i])
"""
price=[[25,30,45,55,60],[45,45,75,90,100],[60,70,110,130,140]]
car = ["4 ล้อ","6 ล้อ","มากกว่า 6 ล้อ"]
print("  โปรแกรมคำนวณค่าผ่านทางมอเตอร์เวย์\n----------------------")
print("รถยนต์ 4 ล้อ       กด 1\nรถยนต์ 6 ล้อ       กด 2\nรถยนต์มากกว่า 6 ล้อ    กด 3\n")
a=int(input("เลือกประเภทยานพาหนะ : "))
print(car[a-1])
print("ลาดกระบัง--->บางบ่อ....."+str(price[a-1][0])+"...บาท")
print("ลาดกระบัง--->บางประกง.."+str(price[a-1][1])+"...บาท")
print("ลาดกระบัง--->พนัสนิคม...."+str(price[a-1][2])+"...บาท")
print("ลาดกระบัง--->บ้านบึง....."+str(price[a-1][3])+"...บาท")
print("ลาดกระบัง--->บางพระ...."+str(price[a-1][4])+"...บาท")