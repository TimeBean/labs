# Круг ограничен окружностью заданной длины. Найти его площадь и диаметр. 

import math

print("Программа для подсчёта параметров круга.\n")

circumference = float(input("Введите длину окружности, которой ограничен круг > "))

raw_diameter = circumference / math.pi
diameter = round(raw_diameter, 2)

print("\nДиаметр равен", diameter)

raw_area = math.pi * (raw_diameter / 2) ** 2
area = round(raw_area, 2)

print("Площадь круга равна", area)
