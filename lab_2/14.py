# Даны действительные числа a, b, c (a != 0). Найти действительные корни
# уравнения ax^2 + bx + c = 0, или выдать сообщение, что действительных корней нет.

import math

print('Программа, для решения уравнения вида аx^2 + bx + с = 0.')

a = float(input('Введите a > '))
b = float(input('Введите b > '))
c = float(input('Введите c > '))

if a == 0:
    print('Это не квадратное уравнение.')
else:
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        x1 = (-b + math.sqrt(discriminant)) / (2 * a)
        x2 = (-b - math.sqrt(discriminant)) / (2 * a)
        
        print(f'Два действительных корня: x1 = {x1}, x2 = {x2}')
    elif discriminant == 0:
        x = -b / (2 * a)
        
        print(f'Один действительный корень: x = {x}')
    else:
        print('Действительных корней нет.')