n = int(input("กรุณากรอกจำนวนครั้งในการรับค่า\n"))
i = 0
sum = 0
while(i < n) :
    x = int(input("กรอกตัวเลข["+str(i+1)+"] :"))
    sum = x + sum
    i += 1
print("ผลรวมค่าที่รับมา = "+str(sum))