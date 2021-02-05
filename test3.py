"""
print("  เลือกเมนูเพื่อทำรายการ\n#########################\n    กด 1 เลือกเหมาจ่าย\n    กด 2 เลือกจ่ายเพิ่ม")
x = input()
y = int(input("กรุณากรอกระยะทาง\n"))
if x == 1 :
    if y < 26 :
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท")
    else :
        print("ค่าใช้จ่ายรวมทั้งหมด 55 บาท")
else :
    if y < 25 :
        print("ค่าใช้จ่ายรวมทั้งหมด 25 บาท")
    else :
        print("ค่าใช้จ่ายรวมทั้งหมด 80 บาท")

n = int(input("กรุณากรอกจำนวนครั้งในการรับค่า\n"))
i = 0
sum = 0
while(i < n) :
    x = int(input("กรอกตัวเลข["+str(i+1)+"] :"))
    sum = x + sum
    i += 1
print("ผลรวมค่าที่รับมา = "+str(sum))

print("ป้อนซื่ออาหารสุดโปรดของคุณ หรือ exit เพื่อออกจากโปรแกรม")
food = []
i = 0
j = 0
while(True):
    food_l = input("อาหารโปรดลำดับที่ "+str(i+1)+"คือ :")
    if food_l == 'exit':
        break
    food.append(food_l)
    i += 1
print("อาหารสุดโปรดของคุณมีดังนี้")
while(j < i):
    print(str(j+1)+"."+food[j]+" ")
    j += 1

data = []
while(True):
    print("   ร้านพอมแพมสุดหล่อ\n  เพิ่ม         [a]\n  แสดง        [s]\n  ออกจากระบบ  [x]")
    pom = input()
    if pom == 'a':
        data_n = input("ป้อนข้อมูลของลูกค้า(รหัส:ชื่อ:จังหวัด)")
        data.append(data_n)
        print("*******ข้อมูลได้เข้าสู่ระบบแล้วครับ*******")
    elif pom == 's':
        print("{0:-<30}".format(""))
        print("รหัส-----------ชิ่อ----------จังหวัด")
        print("{0:-<30}".format(""))
        for i in data:
            data_full = i.split(":")
            print("{}".format(data_full))
    else:
        p = input("ต้องการปิดโปรแกรมใช่หรือไม่ y/n: ")
        if p == 'y':
            print("จบการทำงาน")
            break

score_l = ['90-100','80-89','70-79','60-69','50-59','0-49']
sum_s = [0,0,0,0,0,0]
n = int(input("จำนวนนักเรียนที่คุณต้องการ :"))
i = 0
while i < n:
    score = int(input("คะแนนของนักเรียนคนที่ "+str(i+1)+" :"))
    i +=1
    if score<=100 and score>=90:
        sum_s[0] +=1
    elif score<90 and score>=80:
        sum_s[1] +=1
    elif score<80 and score>=70:
        sum_s[2] +=1
    elif score<70 and score>=60:
        sum_s[3] +=1
    elif score<60 and score>=50:
        sum_s[4] +=1
    else:
        sum_s[5] +=1
for j in range(0,6):
    print(score_l[j],":",sum_s[j]*"*")
"""
def Intro(arg1,arg2 = 'com',arg3 = 'ed',arg4 = 'kku'):
    print("Hello,"+arg1+","+arg2+" "+arg3+" "+arg4)

Intro("Py")
Intro(arg1 = "Py")
Intro(arg1 = "Py", arg3 = "Sci")
Intro(arg1 = "Py", arg4 = "kwy")