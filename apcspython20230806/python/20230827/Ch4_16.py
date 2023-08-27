def c2f(c):
    f = 9 / 5 * c +32
    return f

while True:
    intStr = input("輸入攝氏溫度(q離開):")
    if intStr == 'q':
        print("離開")
        break
    tc = c2f(float(intStr))
    print("攝氏:",intStr,"華氏:",tc)
    
