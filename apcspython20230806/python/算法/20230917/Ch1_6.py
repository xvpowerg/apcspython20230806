def dec_to_bin(num):
    l = []
    while True:
        num,rem =  divmod(num,2)
        l.append(str(rem))
        if num == 0:
            return "".join(l[::-1])
def dec_to_hex(num):
    l = []
    base = ["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F"]
    while True:
        num,rem = divmod(num,16)
        l.append(base[rem])
        if num == 0:
            return "".join(l[::-1])
        
num = int(input("請輸入十進位整數"))
#print("二進位:",dec_to_bin(num))
print("十六進位:",dec_to_hex(num))
