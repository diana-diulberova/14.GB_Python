# year = int(input('Введите год в формате уууу: '))
# if year % 4 != 0:
#     print('Это обычный год')
# elif year % 100 == 0:
#     if year % 400 == 0:
#         print('Это високосный год')
#     else:
#         print('Это обычный год')
# else:
#     print('Это високосный год')


year = int(input('Введите год в формате уууу: '))
if year % 4 != 0 or year % 100 == 0 and year % 400 != 0:
    print('Это обычный год')
else:
    print('Это високосный год')