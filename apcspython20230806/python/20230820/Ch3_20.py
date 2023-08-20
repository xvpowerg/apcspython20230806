height = float(input('請輸入身高，單位為公分: '))
weight = int(input('請輸入體重，單位為公斤: '))
bmi = weight/((height/100)**2)
print(f"bmi: {bmi:.2f}, 判定結果:" , end='')

if bmi > 30:
    print("胖胖")
elif bmi > 25:
    print("過重")
elif bmi > 18.5:
    print("正常")
elif bmi  > 0:
   print("太輕") 
else:
   print("錯誤")
