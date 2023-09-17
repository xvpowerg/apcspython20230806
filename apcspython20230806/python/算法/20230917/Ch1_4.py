"""
for i in range(3000):
    print(i)
"""     
def test1(n):
    if n <= 3:
        print(n)
        test1(n+1)
    print("end:",n)    
test1(1)

