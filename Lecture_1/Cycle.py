# num = float(input('Введите число: '))
# count = 0
# while count < num:
#     print(count)
#     count += 2


# num = float(input('Введите число: '))
# STEP = 2
# limit = num - STEP
# count = -STEP
# while count < limit:
#     count += STEP
#     if count % 12 == 0:
#         continue
#     print(count)


# min_limit = 0
# max_limit = 10
# # while True - это бесконечный цикл в Python. Для его завершения нужна команда break
# while True:
#     print('Введи число между', min_limit, 'и', max_limit, '?')
#     num = float(input())
#     if num < min_limit or num > max_limit:
#         print('Неверно')
#     else:
#         break
# print('Было введено число ', num)


min_limit = 0
max_limit = 10
count = 3
num = None

while count > 0:
    print('Попытка', count)
    count -= 1

    print('Введите число между', min_limit, 'и', max_limit, '?')
    num = float(input())
    if num < min_limit or num > max_limit:
        print('Неверно!')
    else:
        break

else:
    print('Исчерпаны все попытки')
    quit()

print('Было введено число ', num)