my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
print(my_dict.get('two'))
print(my_dict.get('five'))
print(my_dict.get('five', 5))
print(my_dict.get('ten', 5))

spam = my_dict.setdefault('five')
print(f'{spam = } \t {my_dict = }')

eggs = my_dict.setdefault('six', 6)
print(f'{eggs = } \t {my_dict = }')

new_spam = my_dict.setdefault('two')
print(f'{new_spam = } \t {my_dict = }')

new_eggs = my_dict.setdefault('one', 1000)
print(f'{new_eggs = } \t {my_dict = }')



my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
spam = my_dict.popitem()
print(f'{spam=} \t {my_dict= }')
eggs = my_dict.popitem()
print(f'{eggs=} \t {my_dict= }')


my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
spam = my_dict.pop('two')
print(f'{spam=} \t {my_dict= }')
# err = my_dict.pop('six')
# err = my_dict.pop()


my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
my_dict.update(dict(six=6))
print(my_dict)
my_dict.update(dict([('five', 5), ('two', 42)]))
print(my_dict)


my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
new_dict = my_dict | {'five': 5, 'two': 42} | dict(six=6)
print(new_dict)
