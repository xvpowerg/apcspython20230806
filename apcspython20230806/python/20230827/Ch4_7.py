results = {"David":0, "Amy":0, "Sean":0}
candidates = ("David", "Amy", "Sean")
for i in range(5):
    v = input("投給誰:")
    if v not in candidates:
        print("無效")
        continue
    results[v] = results[v] + 1
    
print("結果:")
for name in candidates:
    print(name,results[name],"票")
