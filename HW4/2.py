# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

num = int(input("Введите число: "))
factors_list = []
i = 2
m = num
while i * i <= num:
    if num % i == 0:
        factors_list.append(i)
        num //= i
    else:
        i += 1
factors_list.append(num)
print(f'{m} = {factors_list}')
