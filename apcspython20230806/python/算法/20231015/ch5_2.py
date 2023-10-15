def gcd_r(m,n):
    print(f"({m},{n})",end="")
    if n == 0:
        return m
    else:
        return gcd_r(n,m%n)
n1 = 20
n2 = 14

print(gcd_r(n1,n2))

"""
gcd_r(20,14) 20,14
gcd_r(14,6) 14,6
gcd_r(6,2) 6,2
gcd_r(2,0) 2,0
"""
