Sean,David,Amy = 0,1,2
Ch,En,Ma = 0,1,2
scores = [[70,80,90],
          [60,55,70],
          [77,88,99] ]

print("Sean:",scores[Sean])
print("David:",scores[David][Ma])

scores.sort(key=sum)

print(scores)
