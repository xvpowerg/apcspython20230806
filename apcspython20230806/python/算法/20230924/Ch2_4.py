x = [5,15,25,35,45]
for data in x:
    print("data:",data)
print("=======================")
for i in range(len(x)):    
    print(i,":",x[i])
x.insert(2,100)
print(x)
x.append(200)
print(x)
x[2] = 25
print(x)
x.remove(35)
print(x)

v1 = x.pop(0)
print(v1)
v2 = x.pop()
print(v2)
print(x)
v3 = x.pop(1)
print(v3)
print(x)

