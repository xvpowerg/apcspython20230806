num = int(input("請輸整數:"))
n=2
while n < num:
    if num%n == 0:
        print("不是質數")
        break
    n+=1    
else:
     print("是質數") 
