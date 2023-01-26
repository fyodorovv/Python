# Создайте программу для игры в ""Крестики-нолики"".

import random

board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def gen_board():  # Функция генерации доски
    print("-------")
    for i in board:
        print("|" + i[0] + "|" + i[1] + "|" + i[2] + "|")
        print("-------")


def check():  # Инпут ходов и их проверка
    x = int(input(f"Выберите строку (от 1 до 3): "))
    y = int(input(f"Выберите стобец (от 1 до 3): "))
    while board[x-1][y-1] != " ":
        print("Эта ячейка занята!")
        x = int(input(f"Выберите строку: "))
        y = int(input(f"Выберите стобец: "))
    return x, y


def game(x_o):  # Основная функция
    counter = 0
    while True:
        print(f"Ход {x_o}")
        x, y = check()
        board[x-1][y-1] = x_o
        gen_board()
        if (board[0][0] == "X" and board[0][1] == "X" and board[0][2] == "X") or (board[1][0] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[2][0] == "X" and board[2][1] == "X" and board[2][2] == "X"):
            print(f"Победа {x_o}")
            break
        elif (board[0][0] == "X" and board[1][0] == "X" and board[2][0] == "X") or (board[0][1] == "X" and board[1][1] == "X" and board[1][2] == "X") or (board[0][2] == "X" and board[1][2] == "X" and board[2][2] == "X"):
            print(f"Победа {x_o}")
            break
        elif (board[0][0] == "X" and board[1][1] == "X" and board[2][2] == "X") or (board[0][2] == "X" and board[1][1] == "X" and board[2][0] == "X"):
            print(f"Победа {x_o}")
            break
        if (board[0][0] == "O" and board[0][1] == "O" and board[0][2] == "O") or (board[1][0] == "O" and board[1][1] == "O" and board[1][2] == "O") or (board[2][0] == "O" and board[2][1] == "O" and board[2][2] == "O"):
            print(f"Победа {x_o}")
            break
        elif (board[0][0] == "O" and board[1][0] == "O" and board[2][0] == "O") or (board[0][1] == "O" and board[1][1] == "O" and board[1][2] == "O") or (board[0][2] == "O" and board[1][2] == "O" and board[2][2] == "O"):
            print(f"Победа {x_o}")
            break
        elif (board[0][0] == "O" and board[1][1] == "O" and board[2][2] == "O") or (board[0][2] == "O" and board[1][1] == "O" and board[2][0] == "O"):
            print(f"Победа {x_o}")
            break
        if x_o == "X":  # Смена символа
            x_o = "O"
        else:
            x_o = "X"
        counter += 1
        if counter == 9:
            print("Ничья!")
            break


def main(): 
    gen_board()
    x_o = random.choice(["X", "O"])
    print(f"Первые ходят {x_o}: ")
    game(x_o)


if __name__ == "__main__":
    main()