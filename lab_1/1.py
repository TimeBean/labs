#Даны катеты прямоугольного треугольника. Найти его гипотенузу, периметр и площадь.

import math

first_cathet = int(input("Длина первого катета > "))
second_cathet = int(input("Длина второго катета > "))

raw_hypotenuse = math.sqrt(first_cathet ** 2 + second_cathet ** 2)
print("Гипотинуза треугольника равна ", end='')

hypotenuse = 0

if raw_hypotenuse == round(raw_hypotenuse):
    hypotenuse = round(raw_hypotenuse)
else:
    #огругляем до двух знаков, если это не нужно, убрать.
    hypotenuse = round(raw_hypotenuse, 2) 

print(hypotenuse)
