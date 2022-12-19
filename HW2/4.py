# Задайте список из N элементов, заполненных числами из промежутка[-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.
import random

num = int(input("Введите число: "))
my_list = []
for i in range(num):
    my_list.append(str(random.randrange(-num, num+1)))

print(my_list)
# Тут я решил пойти чуть дальше задания и не просто читать готовый файл, а генерировать его.
# Генерация файла и заполнение его числом из массива с pozN.
f = open('file.txt', 'w')
for i in range(len(my_list)):
    f.write(f"poz{i+1} = {my_list[i]}" + '\n')
f.close()
# Чтение файла и присвоение переменной poz1 число из выбранной позиции.
seach_pos1 = int(input(f"Введите номер позиции от 1 до {num}: "))
a = open('file.txt').read().split('\n')[seach_pos1-1]
for i in range(len(a)):
    if a[i] == "=":
        poz1 = a[i+2:]
# Чтение файла и присвоение переменной poz2 число из выбранной позиции.
seach_pos2 = int(input(f"Введите номер позиции от 1 до {num}: "))
b = open('file.txt').read().split('\n')[seach_pos2-1]
for i in range(len(b)):
    if b[i] == "=":
        poz2 = b[i+2:]

sum = int(poz1)*int(poz2)
print(f"Произведение элементов poz1 = {poz1} и poz2 = {poz2}, равна {sum}")
