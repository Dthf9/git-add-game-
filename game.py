from random import randint

x = randint(1, 10)
attempt = 0

while True:
    print("Я загадалa число от 1 до 10")
    user_num = int(input("Ваша догадка: "))
    attempt += 1
    if attempt > 2:
        print('Ты проиграл.')
        break
    if user_num == x:
        print(f"Ты угадал число, молодец!\nКоличество попыток: {attempt}\nСпасибо за игру")
        break
    elif user_num > x:
        print("Моё число меньше.")
    elif user_num < x:
        print("Моё число больше")
