num = input('輸入一群整數用空白隔開:')
num = map(int,num.split())
myList = list(num)

for k in range(len(myList) - 1):
    if myList[k] * myList[k + 1] >= 0:
        print("不是正負交錯")
        break
else:
    print("正負交錯")
