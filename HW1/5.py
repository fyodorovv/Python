# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21
import math

xa = int(input("Введите Xa: "))
ya = int(input("Введите Ya: "))
xb = int(input("Введите Xb: "))
yb = int(input("Введите Yb: "))

num = math.sqrt((xb - xa)**2 + (yb - ya)**2)
print(num)
