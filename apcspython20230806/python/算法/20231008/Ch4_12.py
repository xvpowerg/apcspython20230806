#是否為質數
def is_prime(number):
    for i in range(2,number):
        if number % i == 0:
            return False
    return True

n = 37
for i in range(2,n+1):
    if is_prime(i):
        print(i)
"""
print(is_prime(5))
print(is_prime(19))
print(is_prime(25))
"""
