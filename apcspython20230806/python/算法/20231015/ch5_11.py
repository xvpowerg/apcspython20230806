import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()

val=0
data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)

while True:
    val=int(input('(1-100)，-1離開：'))
    if val == -1:
        break
    for i in range(50):
        if data[i]==val:
            print(f'找到的index:{i + 1}')
            break
    else:
        print('######不存在######')

print('資料內容：')
showData(data)
