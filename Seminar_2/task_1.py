# Создайте в переменной data список значений разных типов перечислив их через запятую внутри квадратных скобок. 
# Для каждого элемента в цикле выведите:
# * порядковый номер начиная с единицы
# * значение
# * адрес в памяти
# * размер в памяти
# * хэш объекта
# * результат проверки на целое число только если он положительный
# * результат проверки на строку только если он положительный
# Добавьте в список повторяющиеся элементы и сравните на результаты.

import sys

data = [4, 7.8, "string", 6500, "string", frozenset([6]), True, False]

for i, value in enumerate(data, 1):
    print(i, value, id(value), sys.getsizeof(value), hash(value))
    if isinstance(value, str):
        print("Строка")
    if isinstance(value, int):
        print("Целое число")