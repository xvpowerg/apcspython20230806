def s_root1(x):
    i = 1
    while i*i < x:
        i += 1
        if i * i == x:
           return i 
    return i - 1

def s_root2(x,pre=2):
    step = 1
    r = step
    while step >= 10**-pre:
        while(r * r < x ):
            r += step
            if r * r == x:
                return r
        r -= step
        step /= 10
    return r

print(s_root1(4))
print(f"{s_root2(2):.2f}")
