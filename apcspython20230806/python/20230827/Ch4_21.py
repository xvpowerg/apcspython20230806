def personInfo(name,age,**other):
    print("================")
    print("name:",name)
    print("age:",age)
    print("other:",other)
    for k in other:
        print(k,other[k])
    if "email" in other:
        print("發送Email To :",other["email"])
personInfo("Sean",40)
personInfo("Sean",40,phone='025578825')
personInfo("Amy",28,email="amy@gmail.com",company="gj") 
