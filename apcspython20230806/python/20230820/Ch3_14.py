score = 95

if score >= 60:
    print("考試及格")
    if score >= 90:
        print("上台領獎")
else:
   print("不及格")
   if score >= 40:
       print("需要補考")
   else:
       print("明年重修")
print("分數:",score)
