# Даны два действительных числа a, b (a != b). Меньшее из них заменить их полусуммой, а большее – их удвоенным произведением.

print('Программа для вычисления выражения: "Меньшее из чисел заменит их полусуммой, а большее – их удвоенным произведением."')

a = float(input('Введите a > '))
b = float(input('Введите b > '))

half_sum = (a + b) / 2
double_product = 2 * a * b

if a < b:
    a, b = half_sum, double_product
else:
    a, b = double_product, half_sum

print(a, b)