cars = ['honda','BMW','Toyota','audi']
#排序預設小到大
#小寫 > 大寫 > 數字
print(cars)
cars.sort()
print(cars)
cars.sort(reverse = True)#大到小排
print(cars)
cars.sort(key=len)#使用長度排序
print(cars)
cars.sort(key=lambda v:v.upper())#自訂排序
print(cars)


