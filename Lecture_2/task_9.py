DEFAULT = 42
num = int(input("Введите уровень или число ноль для значения по умолчанию: "))
level = num or DEFAULT
print(level)


name = input("Как вас зовут? ")
if name:
    print("Hello, " + name)
else:
    print("Hello, Anonymous")