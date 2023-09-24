myList = []
for i in range(1,1):
 #print(i*i,end=" ")
 myList.append(i*i)
print(myList)

#[1 4 9 16 25 36 49   
#1 2 3 4  5 6   7 .... 10
myList2 = [i**2 for i in range(1,11)]
print(myList2)

myList3 = []
#1~10
for i in range(1,11):
    if i % 2 != 0:
        myList3.append(i)
print(myList3)     
myList4 = [i for i in range(1,11) if i%2 != 0]
print(myList4)
