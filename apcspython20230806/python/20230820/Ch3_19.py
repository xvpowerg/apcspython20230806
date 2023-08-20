num = int(input("輸入整數"))
if num % 2 == 0:
    print("是2的倍數",end = "")
    if num%3 == 0:
       print("是3的倍數") 
else:
   if num % 3 == 0:
       print("是3的倍數")
   else:
       print("不是3與2的倍數")
