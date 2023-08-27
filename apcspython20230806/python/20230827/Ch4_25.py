a = 5
def func():
    a = 10
    print("func():a=",a)

print("呼叫前func():",a)    
func()
print("呼叫後func():",a)
