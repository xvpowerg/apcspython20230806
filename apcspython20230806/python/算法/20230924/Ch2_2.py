a1 = int(input('輸入首項:'))
r = int(input('輸入公比:'))
n = int(input('輸入項數:'))
sum1 = 0
for i in range(n):
    ax = a1 * r ** i
    sum1 += ax
    print(ax,"i:",i,end=" ")
print("=>",sum1)

def getAn(n):
    if n == 1:
        return a1
    else:
        return getAn(n-1) * r

def getSn(n):
    if n == 1:
        return a1
    else:
        an = getAn(n)
        return getSn(n-1) + an             
print(getSn(n))







        
