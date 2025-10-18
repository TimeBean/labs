# Найти сумму и произведение цифр. a) двузначного числа b) трехзначного числа

def sum(number):
    result = 0

    for i in range(len(str(abs(number)))):
        result += number % 10 
        number //= 10   

    return result

def product(number):
    result = 1

    for i in range(len(str(abs(number)))):
        result *= number % 10 

        number //= 10   

    return result

print("Программа для посчёта суммы и произведения цифр числа.\n")

rank_two_number = int(round(float(input("Введите двухзначное число > "))))

if len(str(abs(rank_two_number))) != 2:
    print("Введённое число не двухзначное.")
    exit()

rank_three_number = int(round(float(input("Введите трёхзначное число > "))))

if len(str(abs(rank_three_number))) != 3:
    print("Введённое число не трёхзначное.")
    exit()

print(f"\nСумма цифр двухзначного числа {sum(rank_two_number)}.")
print(f"Сумма цифр трёхзначного числа {sum(rank_three_number)}.\n")

print(f"Произведение цифр двухзначного числа {product(rank_two_number)}.")
print(f"Произведение цифр трёхзначного числа {product(rank_three_number)}.\n")

