my_list = [4, 8, 2, 9, 1, 7, 2]
res = reversed(my_list)
print(type(res), res)
rev_list = list(reversed(my_list))
print(rev_list)

for item in reversed(my_list):
    print(item)


my_list = [4, 8, 2, 9, 1, 7, 2, 5]
my_list.reverse()
print(my_list)

my_list = [4, 8, 2, 9, 1, 7, 2, 5, 7]
new_list = my_list[::-1]
print(my_list, new_list, sep='\n')



my_list = [2, 4, 6, 8, 10, 12, 14, 16, 18]
print(my_list[2:7:2])
print(my_list[:7:2])
print(my_list[2::2])
print(my_list[2:7:2])
print(my_list[2:7:])
print(my_list[8:3:-1])
print(my_list[3::])
print(my_list[:7:])
