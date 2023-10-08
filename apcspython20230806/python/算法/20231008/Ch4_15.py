while True:
    n = int(input("輸入一個整數"))
    if n == -1:
        break;
    print(f"{n}=",end="")
    while n > 1:
        for i in range(2,n+1):
            if n % i == 0:
                n = int(n/i)
                if n == 1:
                    print(f"{i}")
                else:
                    print(f"{i}*",end="")
                break     
    
