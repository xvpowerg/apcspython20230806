num = int(input("輸入整數"))
for i in range(2,num):
    if num % i == 0:
        print("不是質數")
        break
else:
    print("是質數")
    
