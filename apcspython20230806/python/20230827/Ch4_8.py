num = int(input("輸入整數"))

isPr = True
for i in range(2,num):
    if num % i == 0:
        isPr = False
        break
if isPr:
    print("是質數")
else:
    print("不是質數")    
