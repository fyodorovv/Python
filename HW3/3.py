# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19
import math

num_list = []
cut_list = []
while (True):
    num = input("Введите число: ")
    if num == "end":
        break
    num_list.append(float(num))

for i in range(len(num_list)):
    cut = math.modf(num_list[i])
    if cut[0] == 0:
        continue
    cut_list.append(round(cut[0], 2))

raz = (max(cut_list) - min(cut_list))
print(f'{num_list} => {raz}')

