# Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# * Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# * Попробуйте избежать дублирования кода
# в преобразованиях к разным системам счисления
# * Избегайте магических чисел
# * Добавьте аннотацию типов где это возможно

# NUMBER = 100
# SYSTEM_2 = 2
# SYSTEM_8 = 8

# def convert(number: int, system: int) -> str:
#     temp = ''
#     while number > 0:
#         temp = temp + str(number % system)
#         number = number // system
#     # разворот строки
#     return temp[::-1]
    
# print(f'Число 0b{NUMBER} в двоичной системе {bin(NUMBER)}')
# print(convert(NUMBER, SYSTEM_2))

# print(f'Число 0o{NUMBER} в восьмеричной системе {oct(NUMBER)}')
# print(convert(NUMBER, SYSTEM_8))


# NUMBER = 100
# SYSTEM_2 = 2
# SYSTEM_8 = 8

# def convert(number: int, system: int) -> str:
#     temp = list()
#     while number > 0:
#         # конкатенация строк не желательна. список предпочтителен
#         temp.append(str(number % system))
#         number = number // system
#     # разворот строки
#     temp.reverse()
#     return ''.join(temp)
    
# print(f'Число 0b{NUMBER} в двоичной системе {bin(NUMBER)}')
# print(convert(NUMBER, SYSTEM_2))

# print(f'Число 0o{NUMBER} в восьмеричной системе {oct(NUMBER)}')
# print(convert(NUMBER, SYSTEM_8))


def convert(b, c):
    if b == 0:
        return 1
    dig = b % c
    l.append(dig)
    convert(b // c, c)

l = []

a = int(input("Введите число: "))
d = int(input("Введите систему счисления: "))
convert(a, d)
l.reverse()
print("Форма числа по основанию", d)
for i in l:
    print(i, end='')
print('\n')
if d == 2:
    print(bin(a))
elif d == 8:
    print(oct(a))