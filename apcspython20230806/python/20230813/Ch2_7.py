ch = int(input("請輸入國文成績:"))
ma = int(input("請輸入數學成績:"))
en = int(input("請輸入英文成績:"))

total = ch + ma + en

print(ch)
print(type(ch))
print("total:",total)
print("平均分:",total / 3)
print(f"平均分:{total / 3:.2f}")
print("平均分:",round(total / 3,2) )
