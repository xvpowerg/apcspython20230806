scores = [87,66,90,65,70]
scores_sum = 0
counts = len(scores)
score_max = 0
score_min = 100

for i in range(counts):
    print(f"第{i+1}學生分數:{scores[i]}")
    scores_sum += scores[i]
    if  scores[i] > score_max:
        score_max = scores[i]
    if  scores[i] <  score_min:
        score_min = scores[i]
print("Sum:",scores_sum)
print("score_max:",score_max)
print("score_min:",score_min)

print(sum(scores))
print(max(scores))
print(min(scores))
