# Даны катеты прямоугольного треугольника. Найти его гипотенузу, периметр и площадь.

import math

print("Программа для подсчёта параметров прямоугольного треугольника.\n")

first_cathet = int(input("Длина первого катета > "))
second_cathet = int(input("Длина второго катета > "))

raw_hypotenuse = math.sqrt(first_cathet ** 2 + second_cathet ** 2)

hypotenuse = round(raw_hypotenuse, 2) 
print("\nГипотинуза треугольника равна", hypotenuse)

raw_perimeter = first_cathet + second_cathet + raw_hypotenuse

perimeter = round(raw_hypotenuse, 2)

print("Периметр треугольника равен", perimeter)

raw_area = first_cathet * second_cathet / 2

area = round(raw_area, 2)

print("Площадь треугольника равна", area)
