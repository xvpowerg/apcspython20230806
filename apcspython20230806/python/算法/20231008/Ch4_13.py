import math
#是否為質數
def is_prime(number):
    for i in range(2,int(math.sqrt(number) + 1)):
        if number % i == 0:
            return False
    return True

n = 37
for i in range(2,n+1):
    if is_prime(i):
        print(i)
