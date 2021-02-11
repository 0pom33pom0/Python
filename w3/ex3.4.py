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