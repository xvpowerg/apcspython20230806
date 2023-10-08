count = 0

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            for m in range(1,5):
                if i != j and i!=k and k!=j and j!= m and k != m and i != m:
                    count += 1
                    print(f"{count}: {i} {j} {k} {m}")
                
