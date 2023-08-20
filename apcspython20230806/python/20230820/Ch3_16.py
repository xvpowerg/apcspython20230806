#輸入成績
score = int(input("成績"))
#如果>= 60 及格
#否則 不及格
msg = ""
if score >= 60:
    msg = "及格"
else:
    msg = "不及格"
print(msg)    

msg2 = "及格" if score >= 60 else "不及格"
print(msg2)
