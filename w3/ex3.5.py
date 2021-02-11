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