count = 0

for i in range(1,5):
    for j in range(1,5):
        if i == j:
            continue
        for k in range(1,5):
            if k == j or k == i:
                continue
            for m in range(1,5):
                if m== i or m == j or m == k:
                    continue
                count += 1
                print(f"{count}: {i} {j} {k} {m}")
