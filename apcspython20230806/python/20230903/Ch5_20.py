nums = [1,2,3,4]
try:
    10/1
    print(nums[1])
except IndexError:
    print("錯誤的Index")
except ZeroDivisionError:
    print("分母不可為0")
else:
    print("Error沒發生")
