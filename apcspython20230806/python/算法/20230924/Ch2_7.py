myList =[]
for i in range(5):
   myList.append(int(input("請輸入整數:")))
for j in range(len(myList) - 1):
    if myList[j] >= myList[j + 1]:
        print("不是遞增陣列")
        break
else:
    print("是遞增陣列")
