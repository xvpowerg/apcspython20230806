def testScore(s):
    if s < 0 or s > 100:
        raise OverflowError
    if s >= 60:
        return "及格"
    else:
        return "不及格"

print(testScore(10))
print(testScore(70))
print(testScore(-25))
