a = 5
def func():
    global a
    a = a + 1
    print("func():a=",a)
def func2():
    global a
    a = a + 2
    print("func2():a=",a)
    
print("呼叫前func():",a)    
func()
func2()
print("呼叫後func():",a)
