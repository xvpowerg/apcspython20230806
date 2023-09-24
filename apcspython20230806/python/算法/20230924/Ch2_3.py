sum1 = 0
for i in range(1,101):
    sum1 += i
print(sum1)

def inSum(n):
    if n == 1:
        return 1
    else:
        return inSum(n-1) + n
#1+2+3+4
print(inSum(4))    
