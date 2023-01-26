# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# a) Добавьте игру против бота
# b) Подумайте как наделить бота ""интеллектом""

import random


def players1():  # Игра против обычного бота
    allCandy = 2021
    candypl1 = 0
    candypl2 = 0
    player1 = input("Введите имя первого игрока: ")
    player2 = "Bot"
    hod = selecthod(player1, player2)
    while allCandy > 28:
        if hod:
            candytake = checknum()
            allCandy -= candytake
            candypl1 += candytake
            hod = False
            endhod(candytake, candypl2, allCandy, player1)
        else:
            candytake = random.randint(1, 29)
            candypl2 += candytake
            allCandy -= candytake
            hod = True
            endhod(candytake, candypl2, allCandy, player2)
    win(player1, player2, hod)


def players2():  # Игра против человека
    allCandy = 2021
    candypl1 = 0
    candypl2 = 0
    player1 = input("Введите имя первого игрока: ")
    player2 = input("Введите имя второго игрока: ")
    hod = selecthod(player1, player2)
    while allCandy > 28:
        if hod:
            candytake = checknum()
            allCandy -= candytake
            candypl1 += candytake
            hod = False
            endhod(candytake, candypl1, allCandy, player1)
        else:
            candytake = checknum()
            allCandy -= candytake
            candypl2 += candytake
            hod = True
            endhod(candytake, candypl2, allCandy, player2)
    win(player1, player2, hod)


def selecthod(player1, player2):  # Жеребьевка
    hod = random.choice([True, False])
    if hod:
        print(f"По результату жеребьевки первым ходит {player1}")
    else:
        print(f"По результату жеребьевки первым ходит {player2}")
    return hod


def checknum():  # Проверка введенного числа
    maxtake = 28
    num = int(input("Введите кол-во конфет которые хотите забрать: "))
    while num < 1 or num > 28:
        num = int(
            input(f"Нельзя брать конфет больше {maxtake}, возьмите меньше конфет: "))
    return num


def endhod(candytake, candypl1, allCandy, player):  # Информация по концу хода
    print(f"Ходил {player}-игрок, он взял {candytake} конфет, теперь у него {candypl1}. Осталось на столе {allCandy} конфет.")
    print("--------------------------------------------")


def win(player1, player2, hod):  # Определение победетиля
    if hod:
        print(f"Выиграл {player1}")
    else:
        print(f"Выиграл {player2}")


def main():  # Выбор режима игры
    vb = int(input("Выбор игры (1 - Игра против бота) (2 - игра против человека): "))
    if vb == 1:
        players1()
    elif vb == 2:
        players2()
    else:
        print("Ошибка ввода")


if __name__ == "__main__":
    main()
