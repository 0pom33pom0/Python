class nisit :
    def __init__(self,name,sex,year,branch,school,province) :
        self.name = name
        self.sex = sex
        self.year = year
        self.branch = branch
        self.school = school
        self.province = province
    def shownisit(self):
        print(self.sex,self.name,"นักศึกษาชันปีที่",self.year,"สาขา",self.branch,"โรงเรียน",self.school,"จังหวัด",self.province)
print("-"*45,"แนะนำตัว",45*"-")
data_f = input("ชื่อ-นามสกุล:เพศ:ชั้นปีการศึกษา:สาขาวิชา:โรงเรียน:จังหวัด:\t").split(":")
if data_f[1] == 'ชาย':
    data_f[1] = "สวัสดีครับ ผมชื่อ"
else:
    data_f[1 ]= "สวัสดีคะ ดิฉันชื่อ"
x = nisit(data_f[0],data_f[1],data_f[2],data_f[3],data_f[4],data_f[5])
x.shownisit()