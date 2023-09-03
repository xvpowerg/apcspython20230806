try:
    for i in range(1,5):
     print("i:",i,end=" ")
     for k in range(1,5):  
          print("k:",k,end=" ")
          if i == 3: #模擬break
            raise Exception
     print()   
except:
    pass
