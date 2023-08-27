carList = ['Audi', 'Toyota', 'Benz', 'BMW', 'Mazda', 'Ford', 'BMW', 'Benz', 'BMW', 'Mazda']
carSet = set(carList)
print(carSet)

LuxuryCar  = ("Audi", "Benz", "BMW")
LuxuryDict = {"Audi":0, "Benz":0, "BMW":0}
for car in carList :
    if(car in LuxuryCar):
        LuxuryDict[car] = LuxuryDict[car] + 1
print("豪華品牌及數量:", LuxuryDict)
