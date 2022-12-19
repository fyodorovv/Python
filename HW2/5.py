# Реализуйте алгоритм перемешивания списка.
import random

num = int(input("Введите число: "))
my_list = []
for i in range(num):
    my_list.append(str(random.randrange(-num, num+1)))

print(f"Массив до перемешивания: {my_list}")

random.shuffle(my_list)
print(f"Массив после перемешивания: {my_list}")
