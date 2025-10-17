# Дана сторона равностороннего треугольника. Найти его периметр и площадь.

import math

print("Программа для подсчёта параметров равностороннего треугольника.")

side = float(input("Введите длину стороны > "))

raw_perimeter = side * 3
perimeter = round(raw_perimeter, 2)

print("Периметр равен", perimeter)

raw_area = side ** 2 * math.sqrt(3) / 4
area = round(raw_area, 2)

print("Площадь равна", area)
