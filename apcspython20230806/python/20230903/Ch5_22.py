try:
    for i in range(1,10):      
      print(i)
      if i == 5: #模擬break
          raise Exception
except:
    pass
