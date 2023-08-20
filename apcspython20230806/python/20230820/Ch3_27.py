subjs = ["國文","數學","英文"]
scores = [100,80,95]

#利用for幫輸出
"""
國文:100 
數學:80
英文:95
"""
for i in range(len(subjs)):
    print(f"{subjs[i]}:{scores[i]}")

zValue = zip(subjs,scores)
print(list(zValue))

for v1,v2 in zip(subjs,scores):
    print(f"{v1}:{v2}")
