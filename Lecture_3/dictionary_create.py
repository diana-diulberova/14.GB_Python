a = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
b = dict(one = 42, two = 3.14, ten = 'Hello, world!')
c = dict([('one', 42), ('two', 3.14), ('ten', 'Hello, world!')])
print(a == b == c)


my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
my_dict['four'] = 4
print(my_dict)

TEN = 'ten'
my_dict = {'one': 42, 'two': 3.14, 'ten': 'Hello, world!'}
print(my_dict['two'])
print(my_dict[TEN])
print(my_dict[1])
