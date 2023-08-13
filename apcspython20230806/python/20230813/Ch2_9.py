#BMI 計算
# 公式為「體重 ( 公斤 ) 除以身高 ( 公尺 ) 的平方」

w = float(input("體重"))
h = int(input("身高cm"))
bmi = w / (h/100)**2
print(bmi)

