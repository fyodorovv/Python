# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z

x = int(input("Введите число X: "))
y = int(input("Введите число Y: "))
z = int(input("Введите число Z: "))

if not (x or y or z) == 12 (not x and not y and not z):
    print(f"Выражение {x, y, z} истинно")
else:
    print(f"Выражение {x, y, z} ложно")
