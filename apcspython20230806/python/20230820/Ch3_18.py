num = int(input("輸入整數"))
if num % 2 ==0 and num % 3 ==0:
    print("2與3的倍數")
elif num % 2 == 0:
    print("2的倍數")
elif num % 3 == 0:
    print("3的倍數")
else:
    print("不是2與3的倍數")
