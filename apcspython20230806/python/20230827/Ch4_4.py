count = 1
answer = 5
guess = int(input("猜數字"))
while count < 5:
    if guess == answer:
        print("猜對了!")
        break
    count += 1
    guess = int(input("再一次猜數字"))
print("完成")
