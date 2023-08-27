def test(x):
    return x ** 2
list1 =[1,2,3,4,5]
list2 = list(map(test,list1))
print(list2)
