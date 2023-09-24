p = []
p.append([5,6,7])
p.append([8,3,4])
print(p)
print(p[1][2])
#print([""] * 5)
p2 = [[""] * 5 for i in range(10)]
print(p2)
for r in range(10):
    for c in range(5):
        p2[r][c] = f"({r},{c})"

for r in range(10):
    for c in range(5):
        print(p2[r][c],end=" ")
    print()    
