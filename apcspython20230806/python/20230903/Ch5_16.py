scores = {"Ch":100,"En":80,"Ma":95}
print(scores)
print(scores.keys())
print(scores.values())
print(scores.items())
add_dic = {"OS":90}
scores.update(add_dic)
scores["AI"] = 77
print(scores)
scores["Ma"] = 0
print(scores)
print("===================")
print(scores["En"])# Key不存在會拋例外
print(scores.get("Ma"))
print(scores.get("FB",0))#get Key不存在不會拋例外 還可給預設值
print("===================")
print(scores.pop("AI",'Empty'))
print(scores.pop("HI",0))
print(scores)
print("===================")
del scores["Ma"]
print(scores)



