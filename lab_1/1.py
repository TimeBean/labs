#Даны катеты прямоугольного треугольника. Найти его гипотенузу, периметр и площадь.
import math

first_cathet = int(input("Длина первого катета > "))
second_cathet = int(input("Длина второго катета > "))

raw_hypotension = math.sqrt(first_cathet ** 2 + second_cathet ** 2)
print("Гипотинуза треугольника равна ", end='')

hypotension = 0

if raw_hypotension == round(raw_hypotension):
    hypotension = round(raw_hypotension)
else:
    hypotension = round(raw_hypotension, 2)

print(hypotension)
