class MyNumber:
    def __init__(self,n):
     self.n = n
    def __str__(self):
        return str(self.n)
    def __lt__(self,other):#比較小於
        return self.n < other.n
    def __add__(self,other):
        return self.n + other.n
n1 = MyNumber(10)
n2 = MyNumber(15)

print(n1,n2)
ans = n1 < n2
print(ans)
print(n1+n2)
