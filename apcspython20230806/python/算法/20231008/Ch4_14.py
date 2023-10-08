def primeList(number):
    primes = []
    for n in range(2,number+1):
        for i in primes:
            if n % i == 0:
                break
        else:      
            primes.append(n)
    return  primes       

print(primeList(37))
