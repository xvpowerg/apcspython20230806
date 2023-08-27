def weighted_sum(c,e = 80,m = 60):
    return c + e * 2 + m * 3
print(weighted_sum(100,90,70))
print(weighted_sum(100,m = 90))
#只要開始指定名稱參數 後面都要指名參數
print(weighted_sum(e=70,m=51,c=20))
