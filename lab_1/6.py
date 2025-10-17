# Даны три действительных положительных числа. Найти среднее арифметическое и среднее геометрическое этих чисел.

# вообще получилась для посчёта n чисел, но иначе не красиво.

import math

print("Программа для посчёта среднего арифметического и среднего геометрического 3 чисел.\n")

n = 3

values = []

for i in range(1, n + 1):
    value = float(input(f"Введите число {i} > "))

    if value < 0:
        print(f"Проблема: число {i} не положительное")
        break
    else:
        values.append(value)

raw_arithmetic_mean = sum(values) / n
arithmetic_mean = round(raw_arithmetic_mean, 2)

print("\nСреднее арифметическое равно", arithmetic_mean)

raw_geometric_mean = math.prod(values) ** (1 / n)
geometric_mean = round(raw_geometric_mean, 2)

print("Среднее геометрическое равно", geometric_mean)
