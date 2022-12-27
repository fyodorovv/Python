# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:
# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

num_list = []
sum = 0
while(True):
    num = input("Введите число: ")
    if num == "end":
        break       
    num_list.append(int(num))

for i in range(len(num_list)):
    if i % 2 != 0:
        sum += num_list[i]
print(sum)