"""
data=[]
l={}
data_n = input("ป้อนข้อมูลของลูกค้า(รหัส:ชื่อ:จังหวัด)")
data.append(data_n)
for i in data:
    data_full = i.split(",")
    l[1]="{0:<10}{1:<10}{2:<10}".format(int(data_full[0]),data_full[1],data_full[2])
for i in l:
    print(l[i])
print(int(data_full[0])*2)

for i in range(num):
    print("%.4f"% hlt[i]," "+name[i]+" ",int(score[i])," ",int(temes[i]))

print("{0:-<15}\n{1:-<5}{2:-<5}".format("","pom","TL"))

import time
name = []
score = []
temes = []
hlt = []
def time_():
    timeis = time.localtime()
    a = time.strftime('%d %B %Y, %H:%M:%S', timeis)
    print(a)

def input_():
    for i in range(num):
        print("ป้อนข้อมูลคนที่ ",1+i)
        na = input("ชื่อผู้ซ้อม : ")
        sc = float(input("คะแนน : "))
        t = float(input("ระยะเวลำที่ใช้ : "))
        name.append(na)
        score.append(sc)
        temes.append(t)
        hlt.append(sc/t)

def no_():
    for i in range(num):
        j = i
        for j in range(num):
            if hlt[i] > hlt[j]:
                a,b,c,d = hlt[i],name[i],score[i],temes[i]
                hlt[i],name[i],score[i],temes[i] = hlt[j],name[j],score[j],temes[j]
                hlt[j],name[j],score[j],temes[j] = a,b,c,d

def output_():
    print("-"*77)
    print("{0:-<6}{1:-<6}{2:-<8}{3:-<17}{4:-<12}{5:-<15}{6}".format("NO.","PTS","TIME","COMPETITOR#Name","HIT FACTOR","STATE POINTS","STATE PERCENT"))
    print("-"*77)
    for i in range(num):
        stawe_po = (hlt[i]/hlt[0])*50
        stawe_pe = (stawe_po/(hlt[0]/hlt[0]*50))*100
        print("{0: <6}{1: <6}{2: <8}{3: <17}{4: <12}{5: <15}{6}".format(i+1,int(score[i]),"%.2f"%temes[i],name[i],"%.4f"%hlt[i],"%.4f"%stawe_po,"%.2f"%stawe_pe))
    
num = int(input("พิมพ์จำนวนผู้ที่ซ้อมยิงปืน:"))
input_()
no_()
timeis = time.localtime()
a = time.strftime('%A', timeis)
b = time.strftime('%Y', timeis)
print("Shotgun "+a+" Training",b,"\nCondtion : 1")
time_()
output_()

dictionary = {}
def menu():
    global choice
    print(" ")
    print('พจนานุกร\n')
    print(' 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n ')
    choice = input('Input Choice : ')

def เพิ่มคำศัพท์():
    word = input('เพิ่มคำศัพท์ : ')
    type_word = input('ชนิดคำศัพท์(n. , v. , adj. ,) : ' )
    mean = input ('ความหมาย : ')
    dictionary[word] = "{0: <15}{1: <15}".format(type_word,mean)
    print('เพิ่มคำศัพท์เรียบร้อยแล้ว')

def แสดงคำศัพท์():
    print('-'*40)
    print(' '*10+'คำศัพท์ของคุณมีดังนี้'+' '*10)
    print('-'*40)
    print('{0:-<15}{1:-<15}{2:-<8}'.format('คำศัพท์','ประเภท','ความหมาย'))
    for i in dictionary:
        print('{0: <15}{1: <15}'.format(i,dictionary[i]))

while True:
    menu()
    if choice == '1':
       เพิ่มคำศัพท์()
    elif choice == '2':
        แสดงคำศัพท์()

word = {}
def menu():
	print("-"*50)
	print("พจนานุกรม\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n")
def add():
	w = input("เพิ่มคำศัพท์ : " )
	t = input("ชนิดคำศัพท์ (n,v,adj,adv) : ")
	m = input("ความหมาย : ")
	word[w]="{0: <15}{1: <15}".format(t,m)
def view():
	print("-"*50)
	print(" "*20 +"คำศัพท์ของคุณมีดังนี้"+"	"*20)
	print("-"*50)
	print("{0:-<15}{1:-<15}{2:-<10}".format("คำศัพท์" , "ประเภท", "ความหมาย"))
	for i in word:
		print("{0: <15}{1: <15}".format(i,word[i]))
def remove():
	x = input("พิมพ์คำศัพท์ที่ต้องการลบ :")
	z = input("คุณแน่ใจใช่ไหมว่าต้องการลบ (y/n) :")
	if z == "y":
		word.pop(x)
	else:
		print(" ")

while True:
	menu()
	me = int(input("เลือกรายการที่ต้องการ : "))
	if me == 1:
		add()
	elif me == 2:
		view()
	elif me == 3:
		remove()
	else:
		z = input("คุณแน่ใจใช่มั้ยว่าต้องการออกจากโปรแกรม : ")
		if z == "y":
			break
		else:
			print(" ")

import datetime
name,pts,time,hit=[],[],[],[]
num =int(input('Enter number of Competitor     : '))
for i in range(num):
    regname =input('Name of Competitor             : ')
    regpts =int(input('Enter your PTS                 : '))
    regtime =float(input('Enter your time                : '))
    name.insert(i,regname),pts.insert(i,regpts),time.insert(i,regtime),hit.insert(i,pts/time)
for i in range(num):
    j = i
    for j in range(num):
        if pts[i] > pts[j]:
            a,b,c,d = hit[i],name[i],pts[i],time[i]
            hit[i],name[i],pts[i],time[i]=hit[j],name[j],pts[j],time[j]
            hit[j],name[j],pts[j],time[j]=a,b,c,d
date = datetime.datetime.now()
datenew = date.strftime('%G-%m-%d %H:%M:%S')
print('\nShotgun',date.strftime('%A'),'Training',date.strftime('%Y'))
print(datenew)
print('-'*105+'\n{0:-<15}{1:-<15}{2:-<15}{3:-<15}{4:-<15}{5:-<15}{6:-<15}'.format('No.','PTS','TIME','COMPETITOR','HIT FACTOR','STATE POINTS','STATE PERCENT\n'+'-'*105))
for i in range(num):
    print('{0: <15}{1: <15}{2: <15}{3: <15}{4: <15}{5: <15}{6: <15}'.format(i+1,pts[i],time[i],name[i],'%.4f'%hit[i],'%.4f'%float(hit[i]/hit[0]*50),'%.4f'%float((hit[i]/hit[0]*50)/(hit[0]/hit[0]*50)*100)))
"""
word = {}
def menu():
	print("-"*50)
	print("พจนานุกรม\n 1.เพิ่มคำศัพท์\n 2.แสดงคำศัพท์\n 3.ลบคำศัพท์\n 4.ออกจากโปรแกรม\n")
def add():
	w = input("เพิ่มคำศัพท์ : " )
	t = input("ชนิดคำศัพท์ (n,v,adj,adv) : ")
	m = input("ความหมาย : ")
	word[w]="{0: <15}{1: <15}".format(t,m)
def view():
	print("-"*50)
	print(" "*20 +"คำศัพท์ของคุณมีดังนี้"+"	"*20)
	print("-"*50)
	print("{0:-<15}{1:-<15}{2:-<10}".format("คำศัพท์" , "ประเภท", "ความหมาย"))
	for i in word:
		print("{0: <15}{1: <15}".format(i,word[i]))
def remove():
	x = input("พิมพ์คำศัพท์ที่ต้องการลบ :")
	z = input("คุณแน่ใจใช่ไหมว่าต้องการลบ (y/n) :")
	if z == "y":
		word.pop(x)
	else:
		print(" ")

while True:
	menu()
	me = int(input("เลือกรายการที่ต้องการ : "))
	if me == 1:
		add()
	elif me == 2:
		view()
	elif me == 3:
		remove()
	else:
		z = input("คุณแน่ใจใช่มั้ยว่าต้องการออกจากโปรแกรม : ")
		if z == "y":
			break
		else:
			print(" ")
