# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] = > [12, 15, 16]
# - [2, 3, 5, 6] = > [12, 15]
import math

num_list = []
sum_list = []
a = 0
while (True):
    num = input("Введите число: ")
    if num == "end":
        break
    num_list.append(int(num))

for i in range(math.ceil(len(num_list)/2)):
    sum_list.append(num_list[i]*num_list[a-1])
    a -= 1
print(f'{num_list} => {sum_list}')
