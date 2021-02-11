k = 5
vocadulary = {
    "apple":"     n.คำนาม      แอปเปิล",
    "boat":"      n.คำนาม      เรือ",
    "Think":"     v.คำกริยา     คิด",
    "come":"      v.คำกริยา     มา",
    "chair":"     n.คำนาม      เก้าอี้",
}
while(True):
    print("พจนานุกรม\n1) เพิ่มคำศัพท์\n2) แสดงคำศัพท์\n3) ลบคำศัพท์\n4) ออกจากโปรรแกรม\n")
    data = int(input("Tnput Choice :"))
    if data == 1:
        k += 1
        terminology = input("เพิ่มคำศัพท์\t:")
        word_type = input("ชนิดของคำ(n. ,v. ,adj. ,adv. ):")
        if word_type == 'n.':
            word_type = 'n.คำนาม'
        elif word_type == 'v.':
            word_type = 'v.คำกริยา'
        elif word_type == 'adj.':
            word_type = 'adj.คำคุณศัพท์'
        elif word_type == 'adv.':
            word_type = 'adv.คำกริยาวิเศษณ์'
        meaning = input("ความหมาย\t:")
        vocadulary[terminology] = "      "+word_type+"      "+meaning
        print("เพิ่มคำศัพท์เรียบร้อยแล้วครับ")
    elif data == 2:
        print(20*"-"+"\n    คำสัพท์มีทั้งหมด ",k," คำ\n",20*"-")
        print("คำศัพท์      ประเภท      ความหมาย")
        for i in vocadulary:
            print(i+vocadulary[i])
    elif data == 3:
        delete = input("พิมพ์คำศัพท์ที่ต้องการลบ:")
        x = input("ต้องการลบ "+delete+" ใช่หรือไม่(y/n):")
        if x == 'y':
            vocadulary.pop(delete)
            k -= 1
            print("ลบ "+delete+" เรียบร้อยแล้ว")
    else:
        y = input("ต้องการออกจากโปรแกรมใช่หรือไม่(y/n):")
        if y == 'y':
            print("ออกจากโปรแกรมเรียบร้อยแล้ว")
            break