# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

num_list = list(map(int, input("Введите числа через пробел: ").split()))
print(f"Исходный список: {num_list}")
new_list = []
[new_list.append(i) for i in num_list if i not in new_list]
print(f"Список из неповторяющихся элементов: {new_list}")
