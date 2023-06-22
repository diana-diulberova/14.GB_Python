my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
print(my_dict.keys())
for key in my_dict.keys():
    print(key)


my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
print(my_dict.values())
for value in my_dict.values():
    print(value)


my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
print(my_dict.items())
for tuple_data in my_dict.items():
    print(tuple_data)
for key, value in my_dict.items():
    print(f'{key = } value before 100 - {100 - value}')
