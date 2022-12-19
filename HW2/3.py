# Задайте список из n чисел последовательности $(1 +\frac 1 n) ^ n$ и выведите на экран их сумму.
# Пример:
# Для n=4 {1: 2, 2: 2.25, 3: 2.37, 4: 2.44} Сумма 9.06

n = int(input("Введите число: "))
my_list = []
sum = 0
for i in range(1, n+1):
    my_list.append([i, round((1+(1/i))**i, 2)])
dictionary = dict(my_list)
print(f"Для n = {n} {dictionary}")
for key in dictionary:
    sum += dictionary[key]
print(f"Сумма {sum}")
