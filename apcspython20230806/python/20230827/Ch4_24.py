def func(thelist):
    thelist[2] = "Hi"

myList = [10,20,30]
print("呼叫func前:",myList)
func(myList)
print("呼叫func後:",myList)
