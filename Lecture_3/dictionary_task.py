my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
print(my_dict.setdefault('ten', 555))
print(my_dict.values())
print(my_dict.pop('one'))
my_dict['one'] = my_dict['ten']
print(my_dict)
