"""猜数字游戏1~1000"""
import random
number = random.randint(1, 1000)
num_count = 0
while True:
    print("Please enter a number(1~1000): ")
    try:
        guess_number = int(input())
        num_count += 1
        if guess_number > number:
            print("it is greater")
        elif guess_number < number:
            print("it is less")
        else:
            print("Yeah, you get it")
            print("猜测次数为:", num_count)
            break
    except:
        print("请输入一个数字")