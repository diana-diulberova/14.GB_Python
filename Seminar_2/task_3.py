# Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# * Диаметр не превышает 1000 у.е.
# * Точность вычислений должна составлять
# не менее 42 знаков после запятой

import decimal

while True:
    diam = int(input("Введите диаметр окружности: "))
    if diam <= 1000: break

decimal.getcontext().prec = 42
square = decimal.Decimal(3.1415 * diam * diam / 4)
length = decimal.Decimal(3.1415 * diam)
print(f"Площадь круга = {square}")
print(f"Длина окружности = {length}")