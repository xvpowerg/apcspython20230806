class Student: #類別
    def __init__(self,name="empty",age=0):#初始化函
        self.name = name
        self.age = age
    def printInfo(self):
          print(self.name,self.age)
print("AAA")

st1 = Student("Ken",25)#建立Student的物件
#.對物件做寫入或讀取
st1.printInfo()

st2 = Student("Vivin",18)
st2.printInfo()

st3 = Student()
st3.printInfo()
