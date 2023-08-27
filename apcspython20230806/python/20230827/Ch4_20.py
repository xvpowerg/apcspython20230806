def f1(x,y,*z):
    s = x+y
    for v in z:
        s+=v    
    print(x,y,z,"=",s)
f1(1,2)    
f1(1,2,3)
f1(1,2,5,6,7,8)
