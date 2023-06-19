# создание пустого списка
list_1 = list() 

# создание заполненного списка
list_2 = list((3.14, True, "Hello, World!"))

# используем синтаксический сахар:
# создаем пустой список
list_3 = []
# создаем заполненный список
list_4 = [3.14, True, "Hello, World!"]



my_list = [2, 4, 6, 8, 10]

print(my_list[0])
print(my_list[-1])

# Ошибка
# print(my_list(6)) 
# print(my_list[-10])



a = 42
b = "Hello, World!"
c = [1, 2, 3, 4, 5]
my_list = [None]
my_list.append(a)
print(my_list)
my_list.append(b)
print(my_list)
my_list.append(c)
print(my_list)

# Добавляем список в самого себя (циклическая ссылка) - с append так делать не надо!!
my_list.append(my_list)
print(my_list)



a = 42
b = "Hello, World!"
c = [1, 2, 3, 4, 5]
my_list = [None]
# my_list.extend(a) - extend не работает с единичным элементом
print(my_list)
my_list.extend(b)
print(my_list)
my_list.extend(c)
print(my_list)

# Добавляем список в самого себя (циклическая ссылка) - с extend так делать можно, список задвоится
my_list.extend(my_list)
print(my_list)



my_list = [2, 4, 6, 8, 10, 12]
spam = my_list.pop()
print(spam, my_list)
eggs = my_list.pop(1)
print(eggs, my_list)



my_list = [2, 4, 6, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.count(2)
print(spam, my_list)
eggs = my_list.count(3)
print(eggs, my_list)



my_list = [2, 4, 6, 8, 10, 12, 2, 4, 14, 2]
spam = my_list.index(4)
print(spam)
egg = my_list.index(4, 3, 8)
print(egg, my_list)
eggs = my_list.index(4, spam + 1, 90)
print(eggs, my_list)



my_list = [2, 4, 6, 8, 10, 12]
my_list.insert(2, 555)
print(my_list)
my_list.insert(-2, 13)
print(my_list)
my_list.insert(42, 73)
print(my_list)



my_list = [2, 4, 6, 8, 10, 12]
my_list.remove(6)
print(my_list)
my_list.remove(3)
print(my_list)