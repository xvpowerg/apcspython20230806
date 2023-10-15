def fi_r(n):
    if n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    return fi_r(n-1) + fi_r(n-2)

print(fi_r(6))
    
