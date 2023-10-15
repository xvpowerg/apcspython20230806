import random

def showData(data_list):
    for i in range(len(data)//5):
        for j in range(5):
            print('%2d[%3d]  ' %(i*5+j+1,data[i*5+j]),end='')
        print()
data=[]
while(len(data)<50):
    randNum = random.randint(1,100)
    if(randNum not in data):
        data.append(randNum)

data.sort()
print('資料內容：')
showData(data)
def def_search(data,val):
    low,high  = 0,len(data) - 1
    mid = -1
    while not low > high:
        mid = (low+high)//2
        if val < data[mid]:
            high = mid - 1
        elif val > data[mid]:
            low = mid + 1
        else:
            return mid
    return -1

while True:
  val = int(input("請輸入查詢數值-1離開:"))
  if val == -1:
      break
  idx = def_search(data,val)  
  print( idx+1 if idx >= 0 else idx)


            
