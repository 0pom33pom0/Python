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