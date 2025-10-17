# Вычислить расстояние между двумя точками, заданными  своими координатами (x1, y1) и (x2, y2).

import math

# Конечно, класть класс и не-класс в один файл это плохая идея, но для компактности...
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __str__(self):
        return f"({self.x}, {self.y})"

print("Программа для расчёта расстояния между точками.\n")

a_x = float(input("Введите абциссу первой точки > "))
a_y = float(input("Введите ординату первой точки > "))
b_x = float(input("Введите абсциссу второй точки > "))
b_y = float(input("Введите ординату второй точки > "))

first_point = Point(a_x, a_y)
second_point = Point(b_x, b_y)

print("\nПервая точка", first_point)
print("Вторая точка", second_point)

raw_distance = math.sqrt((b_x - a_x) ** 2 + (b_y - a_y) ** 2)
distance = round(raw_distance, 2)

print("\nРасстояние между точками", distance)
