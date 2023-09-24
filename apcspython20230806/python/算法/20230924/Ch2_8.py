num = input('輸入一群整數用空白隔開:')
num = map(int,num.split())
myList = list(num)
for j in range(len(myList) - 1):
    if myList[j]>=myList[j+1]:
        print('不是遞增陣列')
        break
else:
    print('遞增陣列')
