# Дана длина ребра куба. Найти площадь грани, площадь полной поверхности и объем куба.

print("Программа для подсчёта параметров куба.\n")

edge = float(input("Введи длину ребра куба > "))

raw_face_area = edge ** 2
face_area = round(raw_face_area, 2)

print("\nПлощадь ребра куба равна", face_area)

raw_surface_area = raw_face_area * 6
surface_area = round(raw_surface_area, 2)

print("Площадь полной поверхности куба равна", surface_area)

raw_volume = edge ** 3
volume = round(raw_volume, 2)

print("Объём куба равен", volume)
