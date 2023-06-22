name = 'Alex'
age = 12
text = 'Меня зовут %s и мне %d лет' % (name, age)
print(text)

text = 'Меня зовут {} и мне {} лет'.format(name, age)
print(text)

text = f'Меня зовут {name} и мне {age} лет'
print(text)

print(f'{{name}} и {{age}}')



pi = 3.1415
print(f'Число пи с точностью два знака: {pi:.2f}')

data = [32421, 47868778, 2678682, 798879879, 7656784]
for item in data:
    print(f'{item:>10}')

num = 2 * pi * data[1]
print(f'{num = :_}')
