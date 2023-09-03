nums = [1,2,3,4]
try:
    10/0
    print(nums[100])
except IndexError:
    print("錯誤的Index")
except ZeroDivisionError:
    print("分母不可為0")
   
