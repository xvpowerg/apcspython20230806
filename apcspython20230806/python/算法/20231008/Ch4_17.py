minVal = int(input("輸入下限"))
maxVal = int(input("輸入上限")) + 1
for i in range(minVal,maxVal):
    for j in range(i,maxVal):
        for k in range(j,maxVal):
          if i**2 + j**2 == k**2:
              print(f"{i} {j} {k}")
    
